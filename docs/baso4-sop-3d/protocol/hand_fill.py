"""Plate A filled by hand, in drops: one drop stands for the robot's 20 uL, so every well gets 10 drops.

Reads plate_map.csv (the robot protocol's plate A) and writes:
  hand_fill_drops.csv      every well: drops of water, 5 M NaCl, barium chloride and sodium sulfate, and which vial
  hand_fill_sheets.pdf     four letter-size pages, one per pass, with the plate drawn at its real size. Print at
                           100 % ("Actual size"), check the 100 mm bar with a ruler, and stand the plate on the
                           outline: each well's drops show through its clear bottom
  hand_fill_overview.png   the four passes on one image
and prints the per-pass well lists used in fill-by-hand.md.

Every volume in plate_map.csv is a multiple of 20 uL, so the drop counts are exact: the concentrations in a well
depend only on how many of its 10 drops come from each vial, as long as all the drops are the same size.

    python hand_fill.py            (needs matplotlib)
"""
import csv
from collections import OrderedDict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.backends.backend_pdf import PdfPages  # noqa: E402
from matplotlib.patches import Circle, Rectangle  # noqa: E402

HERE = Path(__file__).resolve().parent
UL_PER_DROP = 20.0
DROPS_PER_WELL = 10

# NEST 96 Well Plate 200 uL Flat (Opentrons shared-data nest_96_wellplate_200ul_flat/2.json):
# 127.56 x 85.36 mm, A1 centre 14.28 mm from the left edge and 74.18 mm from the front edge, 9 mm pitch,
# wells 6.85 mm across and 10.8 mm deep (about 400 uL to the brim).
PLATE_W, PLATE_H = 127.56, 85.36
A1_X, A1_Y, PITCH, WELL_D = 14.28, 74.18, 9.0, 6.85
ROWS, COLS = "ABCDEFGH", range(1, 13)

# Where each vial is (SOP: the two printed holders, slots 4 and 5)
VIAL_POS = {("ba", "0.1 M"): "slot 4, A1", ("ba", "10 mM"): "slot 4, A2", ("ba", "1 mM"): "slot 4, A3",
            ("ba", "0.1 mM"): "slot 4, B1", ("so4", "0.1 M"): "slot 5, A1", ("so4", "10 mM"): "slot 5, A2",
            ("so4", "1 mM"): "slot 5, A3", ("so4", "0.1 mM"): "slot 5, B1", ("nacl", "5 M"): "slot 5, B2",
            ("water", ""): "slot 5, B3"}
# Weakest stock first. For the sulfate this puts the slowest wells first and the 3 mM pairs and the 10 mM controls,
# which turn white within minutes, last: they start closest to when the phone does.
STOCK_ORDER = ["0.1 mM", "1 mM", "10 mM", "0.1 M"]

INK, INK2, MUTED, RULE = "#0b0b0b", "#52514e", "#898781", "#c3c2b7"
ACTIVE_FILL = "#cde2fb"      # blue step 100: "this well gets something in this pass"


def col_order_key(well):
    return (int(well[1:]), ROWS.index(well[0]))


def drops(ul):
    n = float(ul or 0) / UL_PER_DROP
    if abs(n - round(n)) > 1e-9:
        raise ValueError(f"{ul} uL is not a whole number of {UL_PER_DROP:.0f} uL drops")
    return int(round(n))


def load():
    wells = OrderedDict()
    with open(HERE / "plate_map.csv", newline="") as f:
        for r in csv.DictReader(f):
            w = {
                "well": r["well"], "role": r["role"], "ba_mM": r["ba_mM"], "so4_mM": r["so4_mM"],
                "nacl_M": r["nacl_M"],
                "water": drops(r["water_uL"]), "nacl": drops(r["nacl_uL"]),
                "ba": drops(r["ba_uL"]), "ba_stock": r["ba_stock"],
                "so4": drops(r["so4_uL"]), "so4_stock": r["so4_stock"],
            }
            total = w["water"] + w["nacl"] + w["ba"] + w["so4"]
            if total != DROPS_PER_WELL:
                raise ValueError(f"{w['well']}: {total} drops, not {DROPS_PER_WELL}")
            wells[w["well"]] = w
    return OrderedDict(sorted(wells.items(), key=lambda kv: col_order_key(kv[0])))


def passes(wells):
    """The four passes, in order, each a list of (heading, vial, [(well, drops), ...])."""
    out = OrderedDict()
    water = OrderedDict()
    for n in sorted({w["water"] for w in wells.values()}, reverse=True):
        water[n] = [(k, n) for k, w in wells.items() if w["water"] == n]
    out["water"] = [(f"{n} drops", ("water", ""), lst) for n, lst in water.items()]
    out["nacl"] = [("2 drops", ("nacl", "5 M"), [(k, w["nacl"]) for k, w in wells.items() if w["nacl"]])]
    for salt in ("ba", "so4"):
        groups = []
        for stock in STOCK_ORDER:
            for n in (1, 3):
                lst = [(k, w[salt]) for k, w in wells.items() if w[f"{salt}_stock"] == stock and w[salt] == n]
                if lst:
                    groups.append((f"{stock}, {n} drop{'s' if n > 1 else ''}", (salt, stock), lst))
        out[salt] = groups
    return out


TITLES = {
    "water": ("Pass 1 of 4: DI water", "vial in slot 5, B3 (its own pipette)"),
    "nacl": ("Pass 2 of 4: 5 M sodium chloride", "vial in slot 5, B2 (its own pipette)"),
    "ba": ("Pass 3 of 4: barium chloride (in the hood)", "slot 4: A1 0.1 M, A2 10 mM, A3 1 mM, B1 0.1 mM; "
           "one pipette per vial"),
    "so4": ("Pass 4 of 4: sodium sulfate, last", "slot 5: A1 0.1 M, A2 10 mM, A3 1 mM, B1 0.1 mM; one pipette "
            "per vial. Weakest vial first"),
}


OVERVIEW_SUB = {
    "water": "vial in slot 5, B3",
    "nacl": "vial in slot 5, B2",
    "ba": "slot 4: A1 0.1 M, A2 10 mM, A3 1 mM, B1 0.1 mM",
    "so4": "slot 5: A1 0.1 M, A2 10 mM, A3 1 mM, B1 0.1 mM",
}


def well_xy(well, ox, oy):
    r, c = ROWS.index(well[0]), int(well[1:]) - 1
    return ox + A1_X + c * PITCH, oy + A1_Y - r * PITCH


def draw_plate(ax, wells, kind, ox, oy, scale_pt=1.0, labels=True, num_fs=12.5, lab_fs=5.6):
    """Draw the plate outline at (ox, oy) in mm, with this pass's drops in each well."""
    ax.add_patch(Rectangle((ox, oy), PLATE_W, PLATE_H, fill=False, lw=0.8 * scale_pt, ec=INK))
    for i, row in enumerate(ROWS):
        ax.text(ox - 2.2, oy + A1_Y - i * PITCH, row, ha="right", va="center", fontsize=8 * scale_pt, color=INK2)
    for c in COLS:
        ax.text(ox + A1_X + (c - 1) * PITCH, oy + PLATE_H + 2.0, str(c), ha="center", va="bottom",
                fontsize=8 * scale_pt, color=INK2)
    for row in ROWS:
        for c in COLS:
            name = f"{row}{c}"
            x, y = well_xy(name, ox, oy)
            w = wells.get(name)
            n = w[kind] if w else 0
            stock = (w.get(f"{kind}_stock") or "") if w else ""
            if not w:
                ax.add_patch(Circle((x, y), WELL_D / 2, fill=False, lw=0.4 * scale_pt, ec=RULE, ls=(0, (1, 1.5))))
                continue
            ax.add_patch(Circle((x, y), WELL_D / 2, fc=ACTIVE_FILL if n else "white", lw=0.5 * scale_pt,
                                ec=INK2 if n else RULE))
            if n:
                dy = 1.0 if (labels and stock) else 0.0
                ax.text(x, y + dy, str(n), ha="center", va="center", fontsize=num_fs, weight="bold", color=INK)
                if labels and stock:
                    ax.text(x, y - 2.3, stock, ha="center", va="center", fontsize=lab_fs, color=INK,
                            weight="bold" if stock == "0.1 M" else "normal")
            else:
                ax.text(x, y, "-", ha="center", va="center", fontsize=7 * scale_pt, color=MUTED)


def sheets(wells, groups, path):
    page_w, page_h = 215.9, 279.4          # US letter, mm
    with PdfPages(path) as pdf:
        for kind in ("water", "nacl", "ba", "so4"):
            fig = plt.figure(figsize=(page_w / 25.4, page_h / 25.4))
            ax = fig.add_axes([0, 0, 1, 1])
            ax.set_xlim(0, page_w)
            ax.set_ylim(0, page_h)
            ax.set_aspect("equal")
            ax.axis("off")
            title, sub = TITLES[kind]
            ax.text(14, page_h - 14, f"Plate A by hand. {title}", fontsize=13, weight="bold", color=INK, va="top")
            ax.text(14, page_h - 21, sub, fontsize=9, color=INK2, va="top")
            ax.text(14, page_h - 26.5, "The big number is how many drops go into that well in this pass. "
                    "Every well ends with 10 drops in all.", fontsize=8.5, color=INK2, va="top")
            ox, oy = (page_w - PLATE_W) / 2, page_h - 40 - PLATE_H - 6
            draw_plate(ax, wells, kind, ox, oy, labels=kind in ("ba", "so4"))
            ax.text(ox, oy - 4, "Stand the plate on this outline, A1 at the top left. A dotted circle is a well "
                    "that stays empty.", fontsize=7.5, color=INK2, va="top")
            # the scale check
            by = oy - 12
            ax.plot([ox, ox + 100], [by, by], color=INK, lw=1.2)
            for x in (ox, ox + 100):
                ax.plot([x, x], [by - 1.5, by + 1.5], color=INK, lw=1.2)
            ax.text(ox + 50, by - 2.5, "This bar should measure 100 mm. If it doesn't, print again at 100 % "
                    "(\"Actual size\", not \"Fit\")", fontsize=7.5, color=INK, va="top", ha="center")
            # the lists, to tick off
            y = by - 11
            total = 0
            for head, vial, lst in groups[kind]:
                n_drops = sum(n for _w, n in lst)
                total += n_drops
                name = {"water": "DI water", "nacl": "5 M NaCl", "ba": "barium chloride",
                        "so4": "sodium sulfate"}[vial[0]]
                line = f"{head} of {name}" if vial[0] in ("water", "nacl") else f"{name} {head}"
                ax.text(14, y, f"{line} ({VIAL_POS[vial]}): {len(lst)} wells", fontsize=8.5, weight="bold",
                        color=INK, va="top")
                y -= 5
                names = [w for w, _n in lst]
                per = 7 if kind == "so4" else 16          # the sulfate list has a blank for each well's time
                for i in range(0, len(names), per):
                    chunk = names[i:i + per]
                    if kind == "so4":
                        txt = "   ".join(f"□ {w:<3} __:__" for w in chunk)
                    else:
                        txt = "   ".join(f"□ {w}" for w in chunk)
                    ax.text(18, y, txt, fontsize=8, color=INK, va="top", family="DejaVu Sans Mono")
                    y -= 5.2 if kind == "so4" else 4.6
                y -= 1.5
            ax.text(14, y - 1, f"{total} drops in this pass.", fontsize=8, color=INK2, va="top")
            if kind == "so4":
                ax.text(14, y - 6, "Each well: its drops, then the time beside its box (__:__), then stir it 5 times "
                        "round with a fresh 300 uL tip. Then the next well.", fontsize=8, color=INK, va="top")
            ax.text(14, 8, "digital-wetlab PR 84, docs/baso4-sop-3d/protocol/hand_fill.py; from plate_map.csv",
                    fontsize=6.5, color=MUTED)
            pdf.savefig(fig)
            plt.close(fig)


def overview(wells, path):
    fig, axes = plt.subplots(2, 2, figsize=(12.8, 9.6), dpi=150)
    fig.patch.set_facecolor("white")
    for ax, kind in zip(axes.flat, ("water", "nacl", "ba", "so4")):
        ax.set_xlim(-8, PLATE_W + 2)
        ax.set_ylim(-3, PLATE_H + 9)
        ax.set_aspect("equal")
        ax.axis("off")
        draw_plate(ax, wells, kind, 0, 0, scale_pt=1.0, labels=kind in ("ba", "so4"), num_fs=12, lab_fs=6.6)
        title, _sub = TITLES[kind]
        ax.set_title(f"{title}\n{OVERVIEW_SUB[kind]}", fontsize=10, color=INK, loc="left")
    fig.suptitle("Plate A by hand: drops into each well, pass by pass (1 drop = the robot's 20 µL; "
                 "10 drops a well)", fontsize=12, weight="bold", color=INK, x=0.02, ha="left")
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(path, facecolor="white")
    plt.close(fig)


def main():
    wells = load()
    groups = passes(wells)
    with open(HERE / "hand_fill_drops.csv", "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["well", "role", "ba_mM", "so4_mM", "nacl_M", "water_drops", "nacl_drops", "ba_drops",
                     "ba_vial", "so4_drops", "so4_vial", "total_drops"])
        for k, w in wells.items():
            wr.writerow([k, w["role"], w["ba_mM"], w["so4_mM"], w["nacl_M"], w["water"], w["nacl"], w["ba"],
                         f"{w['ba_stock']} ({VIAL_POS[('ba', w['ba_stock'])]})" if w["ba"] else "",
                         w["so4"], f"{w['so4_stock']} ({VIAL_POS[('so4', w['so4_stock'])]})" if w["so4"] else "",
                         w["water"] + w["nacl"] + w["ba"] + w["so4"]])
    sheets(wells, groups, HERE / "hand_fill_sheets.pdf")
    overview(wells, HERE / "hand_fill_overview.png")

    # the lists, for fill-by-hand.md
    for kind, rows in groups.items():
        total = sum(n for _h, _v, lst in rows for _w, n in lst)
        print(f"\n## {kind}: {total} drops, {sum(len(lst) for _h, _v, lst in rows)} well-additions")
        for head, vial, lst in rows:
            print(f"- {head} [{VIAL_POS[vial]}] ({len(lst)} wells): {', '.join(w for w, _n in lst)}")
    print(f"\nwells: {len(wells)}; every one {DROPS_PER_WELL} drops")


if __name__ == "__main__":
    main()
