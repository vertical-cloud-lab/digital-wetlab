"""Cut the six SOP parts into one MP4 per step, so each step can be played, paused and replayed on its own.

Asked on issue 80 (2026-11-05): "make all those into different mp4 videos. that way i can pause them when needed".

Each part's `out/<part>.json` gives the frame range of every step in `out/mp4/<part>.mp4`. This script cuts those
ranges frame-exactly, then holds the last frame so the caption stays on screen long enough to read: the clip runs
for at least `len(caption) / READ_CPS + 1` seconds (a subtitle reading speed) and at least 2 s past the motion.
Nothing is re-rendered, so it needs only ffmpeg (on the PATH, or from `pip install imageio-ffmpeg`) and Pillow.

    python3 split_steps.py           # writes out/steps/*.mp4, out/steps/index.json and out/steps/contact_sheet.jpg
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
    "2.2": ("balance-check", "Set up and check the balance", "EB B125, next to the hood"),
    "2.3": ("load-the-hood", "Load the hood, sash down", "EB B125, inside the hood"),
    "2.4": ("tare-the-vial", "Tare the capped vial", "EB B125, next to the hood"),
    "2.5": ("vial-into-hood", "Carry the vial into the hood", "next to, then inside the hood"),
    "2.6": ("uncap-bottle-and-vial", "Uncap the barium chloride and the vial", "EB B125, inside the hood"),
    "2.7": ("spatula-barium-chloride", "Spatula about 366 mg of barium chloride", "EB B125, inside the hood"),
    "2.8": ("cap-and-wipe", "Cap both, wipe the vial", "EB B125, inside the hood"),
    "2.9": ("weigh-the-vial", "Weigh the capped vial and log it", "EB B125, next to the hood"),
    "2.10": ("dissolve-barium-chloride", "Dissolve it and pour into the 0.1 M tube", "EB B125, inside the hood"),
    "2.11": ("make-up-barium-0.1M", "Rinse, make up to 15 mL, invert", "EB B125, inside the hood"),
    "2.12": ("barium-dilutions", "Dilute to 10, 1 and 0.1 mM barium chloride", "EB B125, inside the hood"),
    "2.13": ("cap-and-label-barium", "Cap and label the barium tubes", "EB B125, inside the hood"),
    "2.14": ("weigh-sodium-sulfate", "Weigh about 213 mg of sodium sulfate", "EB B125, next to the hood"),
    "2.15": ("make-up-sodium-sulfate", "Make up the 0.1 M sodium sulfate", "EB B125, next to the hood"),
    "2.16": ("sulfate-nacl-water", "Sulfate dilutions, 5 M NaCl and DI water", "EB B125, next to the hood"),
    "2.17": ("pack-and-clean-up", "Pack the tub and clean up the hood", "EB B125, hood then bench"),
    "3.1": ("before-the-day", "Before the day: calibration, camera, lights", "CB 154"),
    "3.2": ("open-the-door", "Open the OT-2's door", "CB 154, OT-2 deck"),
    "3.3": ("plate-in-slot-7", "Black paper and the plate in slot 7", "CB 154, OT-2 deck"),
    "3.4": ("tips-in-slot-6", "Tips in slot 6", "CB 154, OT-2 deck"),
    "3.5": ("racks-in-slots-4-5", "The racks in slots 4 and 5", "CB 154, OT-2 deck"),
    "3.6": ("uncap-the-tubes", "Uncap the ten tubes", "CB 154, OT-2 deck"),
    "3.7": ("start-capture-then-protocol", "Start the capture job, then the protocol", "CB 154"),
    "3.8": ("fill-water", "Water into 84 wells", "CB 154, OT-2, door closed"),
    "3.9": ("fill-nacl", "5 M NaCl into 64 wells", "CB 154, OT-2, door closed"),
    "3.10": ("fill-barium-chloride", "Barium chloride into 72 wells", "CB 154, OT-2, door closed"),
    "3.11": ("fill-sodium-sulfate-last", "Sodium sulfate last, a new tip per well", "CB 154, OT-2, door closed"),
    "3.12": ("seal-at-the-pause", "Seal the plate at the pause", "CB 154, OT-2 deck"),
    "3.13": ("recap-the-tubes", "Recap the tubes, leave the lights on", "CB 154, OT-2 deck"),
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
    # The last frame of the motion, for the contact sheet.
    thumb = THUMBS / f"{file_stem(row['label'])}.png"
    subprocess.run([ff, "-v", "error", "-y", "-i", str(src), "-vf", f"select=eq(n\\,{row['end_frame']})",
                    "-vframes", "1", str(thumb)], check=True)
    return dst


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

# Shown on the player page. Asked on issue 80 (2026-11-05): shouldn't the OT-2 run be in the fume hood too?
# The README's "Does the OT-2 need to be in the hood?" section has the sources; {readme} is filled in with its URL.
BYU_LCSP = "https://chem.byu.edu/documents/1767/byu_chemical_hygiene_plan.pdf"
HOOD_NOTE = (
    "<b>Does the OT-2 need to be in the hood?</b> Not for this barium plate. A fume hood protects you from what gets "
    "into the air: BYU's <a href=\"" + BYU_LCSP + "\">Laboratory &amp; Chemical Safety Program</a> says to \u201cuse "
    "the fume hood for operations that might result in the release of toxic chemical vapors, fumes or dust\u201d (page "
    "43). Barium chloride <i>powder</i> is that kind of hazard, so its bottle is only opened, weighed from and dissolved "
    "in the hood. Once it is dissolved, nothing comes off it, so the plate is filled on the OT-2 in CB 154 with the door "
    "closed. What is left is the risk of swallowing it or getting it on skin or in the eyes, which gloves, glasses or "
    "goggles, a lab coat and the closed door take care of. <b>Lead and sulfide plates are different:</b> ammonium sulfide "
    "gives off hydrogen sulfide and ammonia, and lead(II) nitrate is a particularly hazardous substance, so the OT-2 "
    "runs inside a hood for those. Sources and caveats: <a href=\"{readme}\">the README</a>."
)
PART_NOTES = {
    "sop3a_load": "In CB 154: lab coat, safety glasses or goggles and nitrile gloves on before the tub is opened, and on "
                  "until the tubes are recapped (3.13). Beside the OT-2: a labelled barium waste bottle, damp wipes and "
                  "a wash bottle of DI water. Wipe up any drip while it is wet, so it never dries to a dust.",
    "sop4_monitor": "At the end of the run (4.5 and 4.6): lab coat, glasses or goggles and gloves on again to take the "
                    "plate out and empty it into the barium waste. Wipe the deck with a damp wipe, then wash your "
                    "hands.",
}


def player_page(rows, sha, readme_sha=None):
    """out/steps/player.html: every step on one page, each in its own player, with its caption written out.

    GitHub can't play an MP4 itself (its file view says "View raw", and raw links download), so the page is opened
    through htmlpreview.github.io, which shows a repo's HTML file as a web page. Each video tries GitHub's raw file
    first, which browsers play inside a <video> tag, then jsDelivr, which serves it as video/mp4 but sometimes refuses
    this repo for being over its 50 MB limit. Both are pinned to `sha`, the commit that added the clips.
    """
    from html import escape

    readme = (f"https://github.com/{REPO}/blob/{readme_sha or sha}/docs/baso4-sop-3d/README.md"
              "#does-the-ot-2-need-to-be-in-the-hood")

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
                f'<p class="dl"><a href="{raw}">download {escape(r["file"])}</a></p></section>')
    whole = " &middot; ".join(
        f'<a href="#w{p}">{escape(PART_TITLES[p])}</a>' for p in PARTS)
    body.append(f'<h2 id="whole">The six parts, and all of it</h2><p>{whole}</p>')
    for p in PARTS + ["baso4_sop_full"]:
        title = PART_TITLES.get(p, "All of it, one part after another (4 min 8 s)")
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
</style></head><body>
<h1>Barium sulfate plate run: the 3-D SOP, one video per step</h1>
<p>Each step has its own player: pause, drag the bar back, or replay it. The step's text is written under each video too.
Every clip ends by holding its last frame, so the text stays up long enough to read.</p>
<p class="note">From <a href="https://github.com/{REPO}/tree/{sha}/docs/baso4-sop-3d">docs/baso4-sop-3d</a>
(issue 80). The time-lapse in step 4.3 is illustrative, not a prediction; the README lists the other assumptions.</p>
<p class="safety">{HOOD_NOTE.format(readme=readme)}</p>
<nav><ul>{"".join(toc)}<li><a href="#whole">The six parts, and all of it</a></li></ul></nav>
{chr(10).join(body)}
<script>
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
    for old in STEPS.glob("*.mp4"):
        old.unlink()
    with ThreadPoolExecutor(max_workers=4) as pool:
        for dst in pool.map(lambda r: cut(ff, r), rows):
            print("wrote", dst.relative_to(HERE))
    index = {"source": "out/<part>.json and out/mp4/<part>.mp4", "read_cps": READ_CPS, "min_tail_s": MIN_TAIL,
             "steps": rows}
    (STEPS / "index.json").write_text(json.dumps(index, indent=1, ensure_ascii=False) + "\n")
    contact_sheet(rows)
    total = sum(r["seconds"] for r in rows)
    print(f"{len(rows)} steps, {total / 60:.1f} min in all")
    print("then commit the clips, and run: python3 split_steps.py --page-only --sha <that commit>")


if __name__ == "__main__":
    main()
