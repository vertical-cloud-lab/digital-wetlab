"""out/barium_dilution_chain.png: step 2.12's three transfers, drawn as a chain of four vials.

Asked on PR 84 (Tim, 2026-11-16): "im taking liquid from the 1m vial and putting that liquid into the other barium
vials?" No: each vial is made from the one before it, and there is no 1 M vial. The caption's old "then 10 into 1,
then 1 into 0.1 mM" left out the units. The amounts are the README's "What goes in each vial". The text is large
and short so that it can still be read on a phone, where the player page shows the picture about 350 px wide; the
steps themselves are in the text around it.

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
GREY = "#4a4e54"

# (label, pocket, how it starts, liquid tint 0..1): the tint only says "weaker"; barium chloride is colourless
VIALS = [
    ("0.1 M", "A1", "powder\n+ water", 0.95),
    ("10 mM", "A2", "13.5 g\nwater", 0.55),
    ("1 mM", "A3", "13.5 g\nwater", 0.30),
    ("0.1 mM", "B1", "13.5 g\nwater", 0.12),
]
TRANSFERS = [("1st", "1.53 g"), ("2nd", "1.50 g"), ("3rd", "1.50 g")]


def main():
    W, H = 9.0, 5.2
    fig = plt.figure(figsize=(W, H), dpi=120)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")

    ax.text(W / 2, H - 0.36, "Each vial is made from the one before it", fontsize=21, weight="bold", color=INK,
            ha="center", va="center")
    ax.text(W / 2, H - 0.80, "The 0.1 M gives only to the 10 mM. There is no 1 M vial.", fontsize=16, color=INK,
            ha="center", va="center")

    xs = [1.15, 3.38, 5.62, 7.85]
    w, y0, h, fill = 1.32, 1.25, 1.75, 1.2    # vial body: width, bottom, height, liquid height
    for x, (conc, pocket, start, tint) in zip(xs, VIALS):
        # liquid, then the glass over it, then the cap
        ax.add_patch(FancyBboxPatch((x - w / 2 + 0.05, y0 + 0.05), w - 0.10, fill,
                                    boxstyle="round,pad=0,rounding_size=0.1", fc=(*BLUE, tint), ec="none", zorder=2))
        ax.add_patch(FancyBboxPatch((x - w / 2, y0), w, h, boxstyle="round,pad=0,rounding_size=0.14",
                                    fc="none", ec=INK, lw=2.4, zorder=3))
        ax.add_patch(Rectangle((x - 0.5, y0 + h), 1.0, 0.3, fc="#3b3f46", ec=INK, lw=1.5, zorder=3))
        ax.text(x, y0 + 0.05 + fill / 2, conc, ha="center", va="center", fontsize=18, weight="bold",
                color="white" if tint > 0.5 else INK, zorder=4)
        ax.text(x, y0 - 0.25, pocket, ha="center", va="center", fontsize=17, weight="bold", color=INK)
        ax.text(x, y0 - 0.52, start, ha="center", va="top", fontsize=14, color=GREY, linespacing=1.15)

    top = y0 + h + 0.36
    for i, (order, grams) in enumerate(TRANSFERS):
        a, b = xs[i] + 0.25, xs[i + 1] - 0.25
        ax.add_patch(FancyArrowPatch((a, top), (b, top), connectionstyle="arc3,rad=-0.42", arrowstyle="-|>",
                                     mutation_scale=28, lw=3.0, color=INK, zorder=5))
        ax.text((xs[i] + xs[i + 1]) / 2, top + 0.62, f"{order}: {grams}", ha="center", va="center", fontsize=18,
                weight="bold", color=INK, bbox=dict(boxstyle="round,pad=0.28", fc="white", ec=BLUE, lw=2.0), zorder=6)

    OUT.parent.mkdir(exist_ok=True)
    fig.savefig(OUT, dpi=120, facecolor="white")
    print(OUT)


if __name__ == "__main__":
    main()
