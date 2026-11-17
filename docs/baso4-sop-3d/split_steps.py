"""Cut the six SOP parts into one MP4 per step, so each step can be played, paused and replayed on its own.

Asked on issue 80 (2026-11-05): "make all those into different mp4 videos. that way i can pause them when needed".

Each part's `out/<part>.json` gives the frame range of every step in `out/mp4/<part>.mp4`. This script cuts those
ranges frame-exactly, then holds the last frame so the caption stays on screen long enough to read: the clip runs
for at least `len(caption) / READ_CPS + 1` seconds (a subtitle reading speed) and at least 2 s past the motion.
Nothing is re-rendered, so it needs only ffmpeg (on the PATH, or from `pip install imageio-ffmpeg`) and Pillow.

    python3 split_steps.py           # writes out/steps/*.mp4, out/steps/index.json and out/steps/contact_sheet.jpg
        [--parts sop2a_hood,sop2b_bench]   # re-cut only these parts' clips; the others stay as they are
    python3 split_steps.py --page-only --sha <commit with the clips>   # writes out/steps/player.html
        [--readme-sha <commit>]   # the README the page's hood note links to (default: the clips' commit)
"""

import json
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "out"
STEPS = OUT / "steps"
THUMBS = HERE / ".cache" / "step_thumbs"  # git-ignored
PARTS = ["sop1_where", "sop2a_hood", "sop2b_bench", "sop3a_load", "sop3b_fill", "sop4_monitor"]
PART_TITLES = {
    "sop1_where": "1. Where each step happens",
    "sop2a_hood": "2a. Barium chloride, inside the hood",
    "sop2b_bench": "2b. Dilutions, then the bench",
    "sop3a_load": "3a. Loading the OT-2 in CB 154",
    "sop3b_fill": "3b. The fill and the seal",
    "sop4_monitor": "4. Watching it for 72 h",
}
READ_CPS = 15.0  # characters per second: a comfortable subtitle reading speed for technical text
MIN_TAIL = 2.0   # seconds held after the motion, at least

# label: (file slug, short title, where it happens). "Where" follows the step table in README.md.
STEP_INFO = {
    "1.1": ("two-rooms", "The two rooms", "overview"),
    "1.2": ("inside-the-hood", "Inside the hood: barium chloride only", "overview"),
    "1.3": ("next-to-the-hood", "Next to the hood: balance and the other salts", "overview"),
    "1.4": ("carry-in-the-tub", "Everything travels capped, in the tub", "overview"),
    "1.5": ("cb154-ot2", "CB 154: uncap only on the OT-2's deck", "overview"),
    "1.6": ("the-order", "The order of the day", "overview"),
    "2.1": ("ppe-and-sds", "PPE and the SDS", "EB B125"),
    "2.2": ("balance-check", "Check the balance; label the vials, weigh them", "EB B125, next to the hood"),
    "2.3": ("load-the-hood", "Load the hood, sash down", "EB B125, inside the hood"),
    "2.4": ("weigh-empty-vial", "Weigh the empty barium chloride vial", "EB B125, next to the hood"),
    "2.5": ("vial-into-hood", "Carry the vial into the hood", "next to, then inside the hood"),
    "2.6": ("uncap-bottle-and-vial", "Uncap the barium chloride and the vial", "EB B125, inside the hood"),
    "2.7": ("spatula-barium-chloride", "Spatula about 312 mg of barium chloride", "EB B125, inside the hood"),
    "2.8": ("cap-and-wipe", "Cap both, wipe the vial", "EB B125, inside the hood"),
    "2.9": ("weigh-the-vial", "Weigh the capped vial and log it", "EB B125, next to the hood"),
    "2.10": ("dissolve-barium-chloride", "Dissolve it in the vial", "EB B125, inside the hood"),
    "2.11": ("weigh-barium-0.1M", "Weigh it, then into the barium holder", "inside, next to, then inside the hood"),
    "2.12": ("barium-dilutions", "Dilute to 10, 1 and 0.1 mM barium chloride, weighing each vial",
             "EB B125, inside the hood, and the balance"),
    "2.13": ("cap-and-label-barium", "Wipe the barium vials, check their labels", "EB B125, inside the hood"),
    "2.14": ("weigh-sodium-sulfate", "Weigh about 213 mg of sodium sulfate", "EB B125, next to the hood"),
    "2.15": ("make-up-sodium-sulfate", "Make up the 0.1 M sodium sulfate", "EB B125, next to the hood"),
    "2.16": ("sulfate-nacl-water", "Sulfate dilutions (weighed), 5 M NaCl and DI water", "EB B125, next to the hood"),
    "2.17": ("pack-and-clean-up", "Pack the tub and clean up the hood", "EB B125, hood then bench"),
    "3.1": ("before-the-day", "Before the day: calibration, camera, lights", "CB 154"),
    "3.2": ("open-the-door", "Open the OT-2's door", "CB 154, OT-2 deck"),
    "3.3": ("plate-on-heater-shaker", "The plate on the heater-shaker in slot 7", "CB 154, OT-2 deck"),
    "3.4": ("tips-in-slot-6", "Tips in slot 6", "CB 154, OT-2 deck"),
    "3.5": ("holders-in-slots-4-5", "The vial holders in slots 4 and 5", "CB 154, OT-2 deck"),
    "3.6": ("uncap-the-vials", "Uncap the ten vials", "CB 154, OT-2 deck"),
    "3.7": ("start-capture-then-protocol", "Start the capture job, then the protocol", "CB 154"),
    "3.8": ("fill-water", "Water into 84 wells", "CB 154, OT-2, door closed"),
    "3.9": ("fill-nacl", "5 M NaCl into 64 wells", "CB 154, OT-2, door closed"),
    "3.10": ("fill-barium-chloride", "Barium chloride into 72 wells", "CB 154, OT-2, door closed"),
    "3.11": ("fill-sodium-sulfate-last", "Sodium sulfate last, a new tip per well", "CB 154, OT-2, door closed"),
    "3.12": ("seal-at-the-pause", "Seal the plate at the pause", "CB 154, OT-2 deck"),
    "3.13": ("recap-the-vials", "Recap the vials, leave the lights on", "CB 154, OT-2 deck"),
    "4.1": ("lid-camera-schedule", "The lid camera and its stills schedule", "CB 154"),
    "4.2": ("camera-view", "What the camera sees", "CB 154"),
    "4.3": ("timelapse-illustrative", "The 72 h time-lapse (illustrative)", "CB 154"),
    "4.4": ("daily-check", "The daily check", "CB 154"),
    "4.5": ("end-of-run", "At 72 h: last still, weigh, photograph", "CB 154"),
    "4.6": ("waste-and-run-record", "Waste and the run record", "CB 154"),
}


def ffmpeg_exe():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
    except ImportError:
        sys.exit("needs ffmpeg on the PATH, or: pip install imageio-ffmpeg")
    return imageio_ffmpeg.get_ffmpeg_exe()


def file_stem(label):
    chapter, step = label.split(".")
    return f"{chapter}-{int(step):02d}"


def plan():
    rows = []
    for part in PARTS:
        meta = json.loads((OUT / f"{part}.json").read_text())
        fps = meta["fps"]
        for s in meta["substeps"]:
            slug, title, where = STEP_INFO[s["label"]]
            n = s["end_frame"] - s["start_frame"] + 1
            motion = n / fps
            total = max(motion + MIN_TAIL, len(s["caption"]) / READ_CPS + 1.0)
            rows.append({
                "label": s["label"],
                "title": title,
                "where": where,
                "part": part,
                "part_title": PART_TITLES[part],
                "file": f"{file_stem(s['label'])}_{slug}.mp4",
                "start_frame": s["start_frame"],
                "end_frame": s["end_frame"],
                "fps": fps,
                "motion_s": round(motion, 2),
                "hold_s": round(total - motion, 2),
                "seconds": round(total, 1),
                "caption": s["caption"],
            })
    return rows


def cut(ff, row):
    src = OUT / "mp4" / f"{row['part']}.mp4"
    dst = STEPS / row["file"]
    vf = (f"trim=start_frame={row['start_frame']}:end_frame={row['end_frame'] + 1},setpts=PTS-STARTPTS,"
          f"tpad=stop_mode=clone:stop_duration={row['hold_s']:.2f}")
    cmd = [ff, "-v", "error", "-y", "-i", str(src), "-vf", vf, "-r", str(row["fps"]), "-an",
           "-c:v", "libx264", "-preset", "slow", "-crf", "24", "-g", str(10 * row["fps"]), "-pix_fmt", "yuv420p",
           "-movflags", "+faststart", "-metadata", f"title=BaSO4 plate run SOP, step {row['label']}: {row['title']}",
           str(dst)]
    subprocess.run(cmd, check=True)
    thumb(ff, row)
    return dst


def thumb(ff, row):
    """The last frame of the step's motion, for the contact sheet."""
    src = OUT / "mp4" / f"{row['part']}.mp4"
    subprocess.run([ff, "-v", "error", "-y", "-i", str(src), "-vf", f"select=eq(n\\,{row['end_frame']})",
                    "-vframes", "1", str(THUMBS / f"{file_stem(row['label'])}.png")], check=True)


def contact_sheet(rows):
    from PIL import Image, ImageDraw, ImageFont

    cols, tw, th, cap = 7, 320, 180, 40
    font_b = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
    head = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 17)
    by_part = [[r for r in rows if r["part"] == p] for p in PARTS]
    # Each part starts a new band of rows, headed by its title.
    layout, y = [], 0
    for part_rows in by_part:
        layout.append(("head", part_rows[0]["part_title"], 0, y))
        y += 28
        for i, r in enumerate(part_rows):
            if i and i % cols == 0:
                y += th + cap + 6
            layout.append(("thumb", r, (i % cols) * (tw + 6), y))
        y += th + cap + 10
    sheet = Image.new("RGB", (cols * (tw + 6) - 6, y), (255, 255, 255))
    d = ImageDraw.Draw(sheet)
    for kind, item, x, yy in layout:
        if kind == "head":
            d.text((x + 4, yy + 5), item, fill=(20, 30, 70), font=head)
            continue
        im = Image.open(THUMBS / f"{file_stem(item['label'])}.png").convert("RGB")
        sheet.paste(im.resize((tw, th), Image.LANCZOS), (x, yy))
        d.text((x + 4, yy + th + 3), f"{item['label']}  {item['seconds']:.0f} s", fill=(30, 50, 120), font=font_b)
        title = item["title"]
        while d.textlength(title, font=font) > tw - 8:
            title = title[:-2].rstrip() + "…"
        d.text((x + 4, yy + th + 21), title, fill=(30, 30, 30), font=font)
    sheet.save(STEPS / "contact_sheet.jpg", quality=86)


REPO = "vertical-cloud-lab/digital-wetlab"
REPO_PATH = "docs/baso4-sop-3d/out"

# Shown on the player page. Asked on issue 80 (2026-11-05): shouldn't the OT-2 run be in the fume hood too? Sterling
# decided on PR 84 (2026-11-06). The README's "Does the OT-2 need to be in the hood?" section has the decision and the
# sources; {readme} is filled in with its URL.
BYU_LCSP = "https://chem.byu.edu/documents/1767/byu_chemical_hygiene_plan.pdf"
HOOD_NOTE = (
    "<b>Does the OT-2 need to be in the hood?</b> Sterling\u2019s call on 11-06: <b>yes, put it in the fume hood</b>, "
    "carried over by two people. Either would probably be fine for this plate, as long as the barium chloride powder is "
    "handled in the hood and the concentrations stay low, but the hood is the safe side. PPE: nitrile gloves, a lab "
    "coat and safety glasses, with long pants and closed-toe shoes. <b>These videos still show the OT-2 in CB 154</b>; "
    "what happens on the deck is the same. The stocks are in 20 mL vials in two printed holders, and the plate sits on "
    "the heater-shaker in slot 7 under the lid camera. The decision, the 11-05 reasoning (BYU\u2019s "
    "<a href=\"" + BYU_LCSP + "\">Laboratory &amp; Chemical Safety Program</a>) and the hood checklist: "
    "<a href=\"{readme}\">the README</a>."
)
# Asked on PR 84 (Tim, 2026-11-16): update the page wherever an amount differs from what the lab is using. The lab's
# barium chloride is anhydrous, and it has no hand pipette, so the dilutions are weighed. Later that day: the HR-100A
# has no TARE key (RE-ZERO is its tare), so every vial is weighed against the empty pan. {salt}, {dil} and {bal} are
# the README's sections on the two forms of the salt, on the dilutions and on the balance.
AMOUNTS_NOTE = (
    "<b>Updated 11-16 for what the lab has.</b> The barium chloride is <b>anhydrous</b>, so spatula about "
    "<b>312 mg</b>, not the dihydrate’s 366 mg (2.7). Weighed against the empty vial (2.4), that’s about 0.3123 g "
    "of salt (2.9), then 15.00 g of water (2.11). <b>The balance has no TARE key</b>: every vial is weighed with "
    "RE-ZERO pressed on the empty pan first, never with a vial on it, and only the weigh boats are tared "
    "(<a href=\"{bal}\">the balance</a>). <b>There is no hand pipette, so the dilutions are weighed</b>: at 2.2 only the "
    "six dilution vials (10, 1 and 0.1 mM of each salt) get water, about 13.5 g each, and each is logged empty and "
    "again with its water; the other four stay dry until their salt is in. Each 1.5 mL goes in with <b>a new disposable "
    "transfer pipette</b>, and each vial is weighed again, capped, before anything is drawn from it (2.12, 2.16). The "
    "balance measures every transfer, so the pipette only has to get close: "
    "<a href=\"{dil}\">how, and the arithmetic</a>. Parts 2a and 2b are re-rendered with these steps and with the "
    "27 × 55 mm vials. The other amounts were already right: 213 mg of sodium sulfate, 4.383 g of NaCl with "
    "13.4 g of water, and the volumes the OT-2 pipettes. A dihydrate bottle would need 366 mg: "
    "<a href=\"{salt}\">why</a>. <b>How much goes in each vial:</b> <a href=\"#vials\">the table below</a>."
)
# Asked on PR 84 (Tim, 2026-11-16, with the six dilution vials holding 13.5 g of water each): how much of each powder
# goes in each vial. Only vials 1, 5 and 9 get powder; the README's "What goes in each vial" has the reasons.
VIAL_HEAD = ("Vial", "Powder", "DI water", "Then", "End reading, above empty")
VIAL_ROWS = [
    ("1. Barium chloride, 0.1 M", "312.3 mg, anhydrous, in the hood (2.5-2.8)", "15.00 g (2.10)", "-", "15.31 g"),
    ("2. Barium chloride, 10 mM", "none", "13.50 g (2.2)", "1.53 g of vial 1 (2.12)", "15.03 g"),
    ("3. Barium chloride, 1 mM", "none", "13.50 g (2.2)", "1.50 g of vial 2 (2.12)", "15.00 g"),
    ("4. Barium chloride, 0.1 mM", "none", "13.50 g (2.2)", "1.50 g of vial 3 (2.12)", "15.00 g"),
    ("5. Sodium sulfate, 0.1 M", "213.1 mg, anhydrous, in a tared boat (2.14)", "15.00 g, rinsing the boat in (2.15)",
     "-", "15.21 g"),
    ("6. Sodium sulfate, 10 mM", "none", "13.50 g (2.2)", "1.52 g of vial 5 (2.16)", "15.02 g"),
    ("7. Sodium sulfate, 1 mM", "none", "13.50 g (2.2)", "1.50 g of vial 6 (2.16)", "15.00 g"),
    ("8. Sodium sulfate, 0.1 mM", "none", "13.50 g (2.2)", "1.50 g of vial 7 (2.16)", "15.00 g"),
    ("9. Sodium chloride, 5 M", "4.383 g, in a tared boat, then into the vial and weighed (2.16)",
     "13.40 g, added on the pan (2.16)", "shake until clear", "17.78 g"),
    ("10. DI water", "none", "about 15 g (15 mL), from a bottle that has only held DI water (2.16)", "-",
     "about 15 g"),
]
VIAL_NOTE = (
    "Only vials 1, 5 and 9 get powder; each dilution vial gets about 1.5 g of the vial before it. Add the last "
    "column to a vial's logged empty reading to get the reading to aim for. The barium chloride needn't be 0.3123 g "
    "(0.28 to 0.33 g is fine): log it, and the stock's real concentration in mol/kg is the salt × 4.802 ÷ the water, "
    "both in grams from the log (0.3051 g with 14.87 g of water is 0.0985). Or add 48.0 g of water per gram of salt "
    "to keep it at 0.1 M. A decahydrate sodium "
    "sulfate bottle needs 483.3 mg and 14.73 g of water. Log every reading the balance shows, not just the amounts: "
    "<a href=\"{vials}\">why, and the details</a>. The NaCl and the DI water vials, step by step: "
    "<a href=\"#s2.16\">under 2.16</a>."
)
PART_NOTES = {
    "sop3a_load": "At the OT-2: nitrile gloves, a lab coat and safety glasses on before the tub is opened, and on "
                  "until the vials are recapped (3.13). Beside the OT-2: a labelled barium waste bottle, damp wipes and "
                  "a wash bottle of DI water. Wipe up any drip while it is wet, so it never dries to a dust.",
    "sop4_monitor": "At the end of the run (4.5 and 4.6): gloves, lab coat and safety glasses on again to take the "
                    "plate out and empty it into the barium waste. Wipe the deck with a damp wipe, then wash your "
                    "hands.",
}


# Under a step's caption on the player page: the step written out in full. Asked on PR 84 (Tim, 2026-11-16) about
# 2.12's caption: "please elaborate on this". The README's "Step 2.12, one transfer at a time" has the same steps and
# the reasons; {how} is filled in with its URL. Later that night Tim asked whether the liquid for the other barium
# vials all comes from one vial ("the 1m vial"): no, it's a chain, so 2.12's note starts with a diagram of it,
# chain_diagram.py's PNG, and {chain} is filled in with its raw URL at the clips' commit. Raw HTML, so no braces
# other than {how} and {chain}.
STEP_NOTES = {
    "2.12": (
        '<div class="how"><b>A chain: each vial is made from the one before it.</b> The 0.1 M vial gives liquid '
        'only to the 10 mM vial; there is no 1 M vial.'
        '<img src="{chain}" alt="0.1 M into 10 mM (about 1.53 g), then 10 mM into 1 mM (1.50 g), then 1 mM into '
        '0.1 mM (1.50 g)" style="display:block;width:100%;max-width:760px;margin:.5em 0">'
        '<b>Step by step</b> (added 11-16). Three transfers, in this order: <b>0.1 M (A1) into '
        '10 mM (A2)</b>, about 1.53 g; <b>10 mM (A2) into 1 mM (A3)</b>, 1.50 g; <b>1 mM (A3) into 0.1 mM (B1)</b>, '
        '1.50 g. Before the first, each water vial needs its &ldquo;with water&rdquo; reading from 2.2 in the log. '
        'For each transfer:<ol>'
        '<li>Read both labels: M or mM?</li>'
        '<li>Uncap both. Each cap goes upside down beside its own vial: every reading includes the cap.</li>'
        '<li>A new transfer pipette. Squeeze the bulb, put the tip in the stronger stock and let go slowly, to a '
        'little past the 1.5&nbsp;mL mark. Lift the tip out of the liquid, still in the vial&rsquo;s mouth, and '
        'squeeze gently down to the mark.</li>'
        '<li>Tip just inside the weaker vial&rsquo;s neck, against the glass. Squeeze all the way, and keep it '
        'squeezed as you lift it out.</li>'
        '<li>The pipette goes in the barium solid waste, never into a second vial.</li>'
        '<li>Cap both. Turn the new vial upside down and back, ten times.</li>'
        '<li>Wipe it with a damp wipe, then dry it with a dry one.</li>'
        '<li>Out to the balance: RE-ZERO with the pan empty, then the vial on, lid closed. Log every digit as '
        '&ldquo;with stock&rdquo;.</li>'
        '<li>&ldquo;With stock&rdquo; minus &ldquo;with water&rdquo; should be about 1.5&nbsp;g. From 1.40 to '
        '1.60&nbsp;g, carry on. Under 1.40&nbsp;g, add a few drops more with a new pipette and weigh it again. Over '
        '1.60&nbsp;g, or a spill: make that vial again with a spare.</li>'
        '<li>Back into its pocket in the hood. Only now is it drawn from, for the next transfer.</li></ol>'
        'Log on paper while your gloves have touched barium, not on a phone. If stock gets on a glove, change the '
        'outer glove in the hood before you carry the vial out. <a href="{how}">Why each step, and the '
        'details</a>.</div>'
    ),
    # Asked on PR 84 (Tim, 2026-11-17): "you never go over what to do with the di water vial or the sodium chloride
    # vials ... you never say how many grams to put in the sodium chloride vial". {nacl} is the README's "Step 2.16:
    # the 5 M NaCl and the DI water vials".
    "2.16": (
        '<div class="how"><b>The sulfate chain, step by step:</b> the same as <a href="#s2.12">2.12</a>, at the '
        'bench, so with no trips in and out of the hood: 0.1 M into 10 mM (about 1.52&nbsp;g), then 10 mM into 1 mM '
        'and 1 mM into 0.1 mM (1.50&nbsp;g each). Weigh each vial before anything is drawn from it. '
        '<a href="{how}">The details</a>.'
        '<p><b>Then the last two vials</b> (added 11-17). Put on fresh gloves, and use a clean spatula, a new weigh '
        'boat and a clean funnel, not the ones from the sodium sulfate. The robot puts the water into all 84 wells '
        'and the NaCl into 64, so a speck of sulfate or barium in either ends up in wells meant to have none.</p>'
        '<p style="margin-bottom:0"><b>Vial 9, sodium chloride, 5&nbsp;M: 4.383&nbsp;g of NaCl, then 13.40&nbsp;g '
        'of DI water</b>, 17.78&nbsp;g above its empty reading (2.2) in all:</p><ol>'
        '<li>Empty pan, lid closed, RE-ZERO. A new weigh boat on the pan, lid closed, RE-ZERO again (this tares '
        'it). Spatula NaCl into the boat to 4.383&nbsp;g (4.36 to 4.41&nbsp;g is fine), and close the bottle. Log the '
        'reading, and the bottle&rsquo;s maker, product number, grade and lot.</li>'
        '<li>Uncap vial 9. Funnel in its neck, tip the salt in, tap the boat and the funnel. Funnel out.</li>'
        '<li>Cap it, weigh it (RE-ZERO with the pan empty first) and log &ldquo;with salt&rdquo;: about 4.38&nbsp;g '
        'above empty.</li>'
        '<li>Uncap it, and put the vial and its cap side by side on the pan. Add DI water until the display reads '
        '&ldquo;with salt&rdquo; plus 13.40&nbsp;g: the wash bottle for most of it, the water-only transfer pipette '
        'for the last drops. Cap it and log &ldquo;with water&rdquo;.</li>'
        '<li>Shake hard until no crystals are left at the bottom. It&rsquo;s nearly saturated, so that takes a few '
        'minutes. It gets a little cold; that&rsquo;s normal.</li>'
        '<li>Into the bench holder, pocket B2.</li></ol>'
        '<p style="margin-bottom:0"><b>Vial 10, DI water: about 15&nbsp;g.</b> The robot takes 10&nbsp;mL of it.'
        '</p><ol>'
        '<li>Fresh DI water, from a bottle that has only held DI water: not the wash bottle that went into the hood.</li>'
        '<li>RE-ZERO with the pan empty, weigh the capped vial empty, and log it.</li>'
        '<li>Uncap it, put the vial and its cap side by side on the pan, and add DI water to about 15&nbsp;g above '
        'the empty reading (14 to 16&nbsp;g is fine).</li>'
        '<li>Cap it straight away, log the reading, and put it in pocket B3.</li></ol>'
        '<a href="{nacl}">Why, and the details</a>.</div>'
    ),
}


def player_page(rows, sha, readme_sha=None):
    """out/steps/player.html: every step on one page, each in its own player, with its caption written out.

    GitHub can't play an MP4 itself (its file view says "View raw", and raw links download), so the page is opened
    through htmlpreview.github.io, which shows a repo's HTML file as a web page. Each video tries GitHub's raw file
    first, which browsers play inside a <video> tag, then jsDelivr, which serves it as video/mp4 but sometimes refuses
    this repo for being over its 50 MB limit. Both are pinned to `sha`, the commit that added the clips.
    """
    import re
    from html import escape

    readme_url = f"https://github.com/{REPO}/blob/{readme_sha or sha}/docs/baso4-sop-3d/README.md"
    readme = readme_url + "#does-the-ot-2-need-to-be-in-the-hood"
    salt = readme_url + "#the-barium-chloride-anhydrous-or-dihydrate"
    dil = readme_url + "#the-dilutions-by-weight-with-transfer-pipettes"
    bal = readme_url + "#the-balance-re-zero-and-what-tare-means"
    vials = readme_url + "#what-goes-in-each-vial"
    how = readme_url + "#step-212-one-transfer-at-a-time"
    nacl = readme_url + "#step-216-the-5-m-nacl-and-the-di-water-vials"
    chain = f"https://raw.githubusercontent.com/{REPO}/{sha}/{REPO_PATH}/barium_dilution_chain.png"
    # the full video is the six parts joined, so its length is theirs
    frames = [json.loads((OUT / f"{p}.json").read_text()) for p in PARTS]
    full_s = round(sum(m["n_frames"] / m["fps"] for m in frames))

    def sources(rel):
        return (f'<source src="https://raw.githubusercontent.com/{REPO}/{sha}/{REPO_PATH}/{rel}" type="video/mp4">'
                f'<source src="https://cdn.jsdelivr.net/gh/{REPO}@{sha}/{REPO_PATH}/{rel}" type="video/mp4">')

    toc, body = [], []
    for part in PARTS:
        part_rows = [r for r in rows if r["part"] == part]
        pid = part.split("_")[0]
        toc.append(f'<li><a href="#{pid}">{escape(PART_TITLES[part])}</a>: '
                   + " ".join(f'<a href="#s{r["label"]}">{r["label"]}</a>' for r in part_rows) + "</li>")
        body.append(f'<h2 id="{pid}">{escape(PART_TITLES[part])}</h2>')
        if part in PART_NOTES:
            body.append(f'<p class="safety">{escape(PART_NOTES[part])}</p>')
        for r in part_rows:
            raw = f"https://github.com/{REPO}/raw/{sha}/{REPO_PATH}/steps/{r['file']}"
            body.append(
                f'<section id="s{r["label"]}"><h3>{r["label"]} &middot; {escape(r["title"])}</h3>'
                f'<p class="where">Where: {escape(r["where"])} &middot; {r["seconds"]:.0f} s</p>'
                f'<video controls playsinline preload="metadata" width="1280" height="720">{sources("steps/" + r["file"])}'
                f'</video><p>{escape(r["caption"])}</p>'
                f'{STEP_NOTES.get(r["label"], "").format(how=how, chain=chain, nacl=nacl)}'
                f'<p class="dl"><a href="{raw}">download {escape(r["file"])}</a></p></section>')
    def cell(text):  # a no-break space keeps each number on the same line as its unit on a phone
        return re.sub(r"(\d) (mg|g|mL|mM|M)\b", "\\1\u00a0\\2", escape(text))

    vial_table = ('<section id="vials"><h2>What goes in each vial</h2><div class="scroll"><table class="vials"><tr>'
                  + "".join(f"<th>{escape(h)}</th>" for h in VIAL_HEAD) + "</tr>"
                  + "".join("<tr>" + "".join(f"<td>{cell(c)}</td>" for c in row) + "</tr>" for row in VIAL_ROWS)
                  + f'</table></div><p class="note">{VIAL_NOTE.format(vials=vials)}</p></section>')
    whole = " &middot; ".join(
        f'<a href="#w{p}">{escape(PART_TITLES[p])}</a>' for p in PARTS)
    body.append(f'<h2 id="whole">The six parts, and all of it</h2><p>{whole}</p>')
    for p in PARTS + ["baso4_sop_full"]:
        title = PART_TITLES.get(p, f"All of it, one part after another ({full_s // 60} min {full_s % 60} s)")
        body.append(f'<section id="w{p}"><h3>{escape(title)}</h3><video controls playsinline preload="none" '
                    f'width="1280" height="720">{sources("mp4/" + p + ".mp4")}</video></section>')
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Barium sulfate plate run: the 3-D SOP, one video per step</title>
<style>
body {{ font: 16px/1.45 system-ui, sans-serif; max-width: 980px; margin: 0 auto; padding: 0 14px 60px; color: #222; }}
h1 {{ font-size: 1.5em; }} h2 {{ margin-top: 2em; border-bottom: 2px solid #2a3d8f; color: #14205a; }}
h3 {{ margin: 1.4em 0 .2em; }} video {{ width: 100%; height: auto; background: #000; border-radius: 6px; }}
.where {{ margin: 0 0 .4em; color: #2a3d8f; font-weight: 600; }} .dl {{ font-size: .9em; }} .note {{ color: #555; }}
.safety {{ background: #fff4dc; border-left: 4px solid #c97a00; padding: .6em .9em; border-radius: 4px; }}
nav li {{ margin: .2em 0; }}
.scroll {{ overflow-x: auto; }} .vials {{ border-collapse: collapse; font-size: .85em; }}
.vials th, .vials td {{ border: 1px solid #ccc; padding: .25em .35em; text-align: left; vertical-align: top; }}
.vials th {{ background: #eef1fb; }}
.how {{ background: #eef4ff; border-left: 4px solid #2a3d8f; padding: .6em .9em; border-radius: 4px; }}
.how ol {{ margin: .4em 0 .4em 1.3em; padding: 0; }} .how li {{ margin: .2em 0; }}
</style></head><body>
<h1>Barium sulfate plate run: the 3-D SOP, one video per step</h1>
<p>Each step has its own player: pause, drag the bar back, or replay it. The step's text is written under each video too.
Every clip ends by holding its last frame, so the text stays up long enough to read.</p>
<p class="note">From <a href="https://github.com/{REPO}/tree/{sha}/docs/baso4-sop-3d">docs/baso4-sop-3d</a>
(issue 80). The time-lapse in step 4.3 is illustrative, not a prediction; the README lists the other assumptions.</p>
<p class="safety">{AMOUNTS_NOTE.format(salt=salt, dil=dil, bal=bal)}</p>
{vial_table}
<p class="safety">{HOOD_NOTE.format(readme=readme)}</p>
<nav><ul><li><a href="#vials">What goes in each vial</a></li>{"".join(toc)}<li><a href="#whole">The six parts, and all of it</a></li></ul></nav>
{chr(10).join(body)}
<script>
// htmlpreview rewrites every link with a # in it to point at this page, which turned the links to the README's
// sections into dead links. This script runs after that rewrite, so it puts them back from data-href.
document.querySelectorAll("a[data-href]").forEach(function (a) {{ a.href = a.getAttribute("data-href"); }});
// Open at the step named in the link (player.html#s2.7), also when the page is shown through htmlpreview.
function goToStep() {{
  const el = document.getElementById(decodeURIComponent(location.hash.slice(1)));
  if (el) el.scrollIntoView();
}}
goToStep();
window.addEventListener("hashchange", goToStep);
</script>
</body></html>
"""
    # keep a copy of each link to another page's section, for the script above to restore under htmlpreview
    page = re.sub(r'<a href="(https://[^"#]*#[^"]*)"', r'<a href="\1" data-href="\1"', page)
    (STEPS / "player.html").write_text(page)


def main():
    if "--page-only" in sys.argv:  # rewrite player.html for clips already committed at --sha <commit>
        readme_sha = sys.argv[sys.argv.index("--readme-sha") + 1] if "--readme-sha" in sys.argv else None
        player_page(plan(), sys.argv[sys.argv.index("--sha") + 1], readme_sha)
        return
    ff = ffmpeg_exe()
    STEPS.mkdir(parents=True, exist_ok=True)
    THUMBS.mkdir(parents=True, exist_ok=True)
    rows = plan()
    # --parts: re-cut only the parts that were re-rendered, so the other clips keep their committed bytes
    redo = set(sys.argv[sys.argv.index("--parts") + 1].split(",")) if "--parts" in sys.argv else set(PARTS)
    unknown = redo - set(PARTS)
    if unknown:
        sys.exit(f"unknown part(s): {', '.join(sorted(unknown))}; the parts are {', '.join(PARTS)}")
    names = {r["file"] for r in rows}
    for old in STEPS.glob("*.mp4"):
        if old.name not in names or any(r["file"] == old.name and r["part"] in redo for r in rows):
            old.unlink()
    with ThreadPoolExecutor(max_workers=4) as pool:
        for dst in pool.map(lambda r: cut(ff, r), [r for r in rows if r["part"] in redo]):
            print("wrote", dst.relative_to(HERE))
        list(pool.map(lambda r: thumb(ff, r), [r for r in rows if r["part"] not in redo]))
    missing = [r["file"] for r in rows if not (STEPS / r["file"]).exists()]
    if missing:
        sys.exit(f"no clip for {', '.join(missing)}: re-cut their parts with --parts")
    index = {"source": "out/<part>.json and out/mp4/<part>.mp4", "read_cps": READ_CPS, "min_tail_s": MIN_TAIL,
             "steps": rows}
    (STEPS / "index.json").write_text(json.dumps(index, indent=1, ensure_ascii=False) + "\n")
    contact_sheet(rows)
    total = sum(r["seconds"] for r in rows)
    print(f"{len(rows)} steps, {total / 60:.1f} min in all")
    print("then commit the clips, and run: python3 split_steps.py --page-only --sha <that commit>")


if __name__ == "__main__":
    main()
