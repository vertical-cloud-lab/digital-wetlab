"""out/barium_dilution_chain.png: step 2.12's three transfers, drawn as a chain of four vials.

Asked on PR 84 (Tim, 2026-11-16): "im taking liquid from the 1m vial and putting that liquid into the other barium
vials?" No: each vial is made from the one before it, and there is no 1 M vial. The caption's old "then 10 into 1,
then 1 into 0.1 mM" left out the units. The amounts are the README's "What goes in each vial".

    python3 chain_diagram.py        # matplotlib only
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle  # noqa: E402

OUT = Path(__file__).resolve().parent / "out" / "barium_dilution_chain.png"
BLUE = (0x2A / 255, 0x3D / 255, 0x8F / 255)   # the player page's blue note
INK = "#1d1d22"
GREY = "#5a5e64"

# (label, pocket, how it starts, liquid tint 0..1): the tint only says "weaker", barium chloride is colourless
VIALS = [
    ("0.1 M", "A1", "312 mg of powder and\nabout 15 g of water (2.4-2.11)", 0.95),
    ("10 mM", "A2", "13.5 g of water (2.2)", 0.55),
    ("1 mM", "A3", "13.5 g of water (2.2)", 0.30),
    ("0.1 mM", "B1", "13.5 g of water (2.2)", 0.12),
]
TRANSFERS = [("1st", "about 1.53 g"), ("2nd", "1.50 g"), ("3rd", "1.50 g")]


def main():
    fig = plt.figure(figsize=(12, 6.7), dpi=110)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.7)
    ax.axis("off")

    ax.text(0.35, 6.3, "Step 2.12: each barium vial is made from the one before it", fontsize=19, weight="bold",
            color=INK, va="center")
    ax.text(0.35, 5.88, "Three transfers, in this order. The 0.1 M vial gives liquid only to the 10 mM vial. "
            "There is no 1 M vial.", fontsize=12.5, color=INK, va="center")

    xs = [1.65, 4.55, 7.45, 10.35]
    w, y0, h, fill = 1.25, 1.85, 2.25, 1.55    # vial body: width, bottom, height, liquid height
    for x, (conc, pocket, start, tint) in zip(xs, VIALS):
        # liquid, then the glass over it, then the cap
        ax.add_patch(FancyBboxPatch((x - w / 2 + 0.06, y0 + 0.06), w - 0.12, fill, boxstyle="round,pad=0,rounding_size=0.12",
                                    fc=(*BLUE, tint), ec="none", zorder=2))
        ax.add_patch(FancyBboxPatch((x - w / 2, y0), w, h, boxstyle="round,pad=0,rounding_size=0.16",
                                    fc="none", ec=INK, lw=2.2, zorder=3))
        ax.add_patch(Rectangle((x - 0.5, y0 + h), 1.0, 0.36, fc="#3b3f46", ec=INK, lw=1.5, zorder=3))
        on_dark = tint > 0.5
        ax.text(x, y0 + 0.06 + fill / 2, conc, ha="center", va="center", fontsize=17, weight="bold",
                color="white" if on_dark else INK, zorder=4)
        ax.text(x, y0 - 0.28, f"pocket {pocket}", ha="center", va="center", fontsize=12, weight="bold", color=INK)
        ax.text(x, y0 - 0.55, start, ha="center", va="top", fontsize=10.5, color=GREY, linespacing=1.3)

    top = y0 + h + 0.42
    for i, (order, grams) in enumerate(TRANSFERS):
        a, b = xs[i] + 0.25, xs[i + 1] - 0.25
        ax.add_patch(FancyArrowPatch((a, top), (b, top), connectionstyle="arc3,rad=-0.45", arrowstyle="-|>",
                                     mutation_scale=26, lw=2.6, color=INK, zorder=5))
        mid = (xs[i] + xs[i + 1]) / 2
        ax.text(mid, top + 0.8, f"{order}: {grams}", ha="center", va="center", fontsize=13.5, weight="bold",
                color=INK, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=BLUE, lw=1.6), zorder=6)

    ax.text(0.35, 0.36, "After each transfer: cap it, invert it ten times, wipe it damp then dry, weigh it and log "
            "“with stock”. Only then draw from it.\n"
            "About 1.5 mL each: a new transfer pipette, drawn to its 1.5 mL mark. 2.16 is the same chain for sodium "
            "sulfate (about 1.52 g, then 1.50 g, 1.50 g).", fontsize=10.8, color=INK, va="center", linespacing=1.45)

    OUT.parent.mkdir(exist_ok=True)
    fig.savefig(OUT, dpi=110, facecolor="white")
    print(OUT)


if __name__ == "__main__":
    main()
