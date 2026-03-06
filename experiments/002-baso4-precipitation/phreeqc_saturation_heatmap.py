"""
PHREEQC Saturation Index Predictions for BaSO₄ Precipitation Experiment
========================================================================

Uses PHREEQC with the Pitzer activity-coefficient model to predict the
saturation index (SI) of barite (BaSO₄) in each of the 96 wells of
Experiment 002.  Wells 1–80 are Latin-hypercube-sampled conditions;
wells 81–96 are controls.

SI > 0  →  supersaturated (precipitation expected)
SI = 0  →  at equilibrium
SI < 0  →  undersaturated (no precipitation)

Outputs
-------
- experiments/002-baso4-precipitation/baso4_saturation_heatmap.png
  Plate-layout heatmap with diverging RdBu_r colorscale centred on SI = 0.
"""

import os
import numpy as np
from scipy.stats import qmc
from phreeqpython import PhreeqPython
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
import matplotlib.patches as mpatches

# ---------------------------------------------------------------------------
# 1. Generate the 80 LHS conditions  (must match experiment design exactly)
# ---------------------------------------------------------------------------
sampler = qmc.LatinHypercube(d=3, seed=42)
sample = sampler.random(n=80)

l_bounds = [0.1, 0.1, 0.0]   # [Ba²⁺ mM, SO₄²⁻ mM, NaCl molal]
u_bounds = [50.0, 50.0, 3.0]
lhs = qmc.scale(sample, l_bounds, u_bounds)

# ---------------------------------------------------------------------------
# 2. Build the full 96-well condition table
#    Column-major ordering:  A1, B1, …, H1, A2, B2, …, H10  →  wells 1–80
#    Wells 81–96 are controls (see Experiment 002 README)
# ---------------------------------------------------------------------------
# Rows A–H  =  0–7,   Columns 1–12  =  0–11
ROWS = "ABCDEFGH"

well_labels = []
ba_mM  = np.zeros(96)
so4_mM = np.zeros(96)
nacl_m = np.zeros(96)
well_type = [""] * 96   # 'LHS', 'Ba-only', 'SO4-only', 'blank', 'positive'

# Wells 1–80: LHS conditions (column-major: A1 B1 … H1 A2 B2 … H10)
for idx in range(80):
    col = idx // 8       # 0-based column
    row = idx % 8        # 0-based row
    label = f"{ROWS[row]}{col+1}"
    well_labels.append(label)
    ba_mM[idx]  = lhs[idx, 0]
    so4_mM[idx] = lhs[idx, 1]
    nacl_m[idx] = lhs[idx, 2]
    well_type[idx] = "LHS"

# Wells 81–84: Ba²⁺-only negatives (column 11: A11–D11)
for i, row_idx in enumerate(range(4)):
    idx = 80 + i
    label = f"{ROWS[row_idx]}11"
    well_labels.append(label)
    ba_mM[idx]  = 25.0     # mid-range Ba²⁺
    so4_mM[idx] = 0.0
    nacl_m[idx] = 1.5      # mid-range NaCl
    well_type[idx] = "Ba-only"

# Wells 85–88: SO₄²⁻-only negatives (column 11: E11–H11)
for i, row_idx in enumerate(range(4, 8)):
    idx = 84 + i
    label = f"{ROWS[row_idx]}11"
    well_labels.append(label)
    ba_mM[idx]  = 0.0
    so4_mM[idx] = 25.0     # mid-range SO₄²⁻
    nacl_m[idx] = 1.5
    well_type[idx] = "SO4-only"

# Wells 89–92: Blanks (column 12: A12–D12)
for i, row_idx in enumerate(range(4)):
    idx = 88 + i
    label = f"{ROWS[row_idx]}12"
    well_labels.append(label)
    ba_mM[idx]  = 0.0
    so4_mM[idx] = 0.0
    nacl_m[idx] = 1.5
    well_type[idx] = "blank"

# Wells 93–96: Positive controls (column 12: E12–H12)
for i, row_idx in enumerate(range(4, 8)):
    idx = 92 + i
    label = f"{ROWS[row_idx]}12"
    well_labels.append(label)
    ba_mM[idx]  = 50.0     # max Ba²⁺
    so4_mM[idx] = 50.0     # max SO₄²⁻
    nacl_m[idx] = 0.0      # no NaCl (highest supersaturation)
    well_type[idx] = "positive"

# ---------------------------------------------------------------------------
# 3. Run PHREEQC with Pitzer for each well
# ---------------------------------------------------------------------------
db_path = os.path.join(
    os.path.dirname(os.path.abspath(__import__("phreeqpython").__file__)),
    "database", "pitzer.dat"
)
pp = PhreeqPython(database=db_path)

si_values = np.full(96, np.nan)

for idx in range(96):
    ba  = ba_mM[idx]    # mmol/L  (phreeqpython expects mmol/kgw ≈ mmol/L for dilute)
    so4 = so4_mM[idx]
    na_cl = nacl_m[idx] * 1000  # molal → mmol/kgw

    # Build PHREEQC solution
    soln_dict = {}
    if ba > 0:
        soln_dict["Ba"] = ba
    if so4 > 0:
        soln_dict["S(6)"] = so4
    if na_cl > 0:
        soln_dict["Na"] = na_cl
        soln_dict["Cl"] = na_cl
    # Also include small Cl⁻ from BaCl₂  (2× Ba²⁺ in mM)
    if ba > 0:
        soln_dict["Cl"] = soln_dict.get("Cl", 0) + 2 * ba

    if ba > 0 and so4 > 0:
        sol = pp.add_solution(soln_dict)
        si_values[idx] = sol.si("Barite")
    elif ba == 0 or so4 == 0:
        # No barite can form — SI is effectively −∞; we'll mark as very undersaturated
        si_values[idx] = -10.0

print("SI range:", np.nanmin(si_values), "to", np.nanmax(si_values))

# ---------------------------------------------------------------------------
# 4. Build 8×12 grid for the 96-well plate
# ---------------------------------------------------------------------------
si_grid = np.full((8, 12), np.nan)

for idx in range(96):
    label = well_labels[idx]
    row = ROWS.index(label[0])
    col = int(label[1:]) - 1
    si_grid[row, col] = si_values[idx]

# ---------------------------------------------------------------------------
# 5. Create the heatmap figure
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 6))

# Diverging norm centred at 0
vmin = np.nanmin(si_grid[si_grid > -10])  # exclude −10 sentinel
vmax = np.nanmax(si_grid)
# Clamp negative sentinel wells to vmin for display
si_display = si_grid.copy()
si_display[si_display <= -9] = vmin - 1  # push controls below color range

norm = TwoSlopeNorm(vmin=min(vmin, -1), vcenter=0, vmax=max(vmax, 1))

im = ax.imshow(si_display, cmap="RdBu_r", norm=norm, aspect="equal")

# Add text annotations
for r in range(8):
    for c in range(12):
        val = si_grid[r, c]
        label = f"{ROWS[r]}{c+1}"
        if val <= -9:
            txt = "ctrl"
            color = "gray"
        else:
            txt = f"{val:.1f}"
            color = "white" if abs(val) > (vmax * 0.5) else "black"
        ax.text(c, r, txt, ha="center", va="center", fontsize=7, color=color, fontweight="bold")

# Axis labels
ax.set_xticks(range(12))
ax.set_xticklabels([str(i+1) for i in range(12)], fontsize=10)
ax.set_yticks(range(8))
ax.set_yticklabels(list(ROWS), fontsize=10)
ax.set_xlabel("Column", fontsize=12)
ax.set_ylabel("Row", fontsize=12)
ax.set_title(
    "BaSO₄ Saturation Index (Pitzer) — 96-Well Plate Layout\n"
    "SI > 0: supersaturated (precipitation expected)  •  SI < 0: undersaturated",
    fontsize=13, fontweight="bold"
)

# Colorbar
cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
cbar.set_label("Saturation Index (SI) — Barite [BaSO₄]", fontsize=11)

# Legend for control wells
patches = [
    mpatches.Patch(facecolor="white", edgecolor="gray", label="ctrl = negative/blank control (SI undefined)"),
]
ax.legend(handles=patches, loc="lower right", fontsize=8, framealpha=0.9)

plt.tight_layout()
out_path = os.path.join(os.path.dirname(__file__), "baso4_saturation_heatmap.png")
fig.savefig(out_path, dpi=200, bbox_inches="tight")
print(f"Saved: {out_path}")

# ---------------------------------------------------------------------------
# 6. Print summary table for key wells mentioned in PR discussion
# ---------------------------------------------------------------------------
print("\n=== Key Wells ===")
for label in ["G1", "H1", "F3", "G3"]:
    row = ROWS.index(label[0])
    col = int(label[1:]) - 1
    idx_in_96 = col * 8 + row  # column-major
    if idx_in_96 < 80:
        print(f"  {label}: Ba²⁺ = {ba_mM[idx_in_96]:.2f} mM, "
              f"SO₄²⁻ = {so4_mM[idx_in_96]:.2f} mM, "
              f"NaCl = {nacl_m[idx_in_96]:.3f} m, "
              f"SI(Barite) = {si_values[idx_in_96]:.3f}")

# Print statistics
lhs_si = si_values[:80]
print(f"\nLHS wells (1-80) SI statistics:")
print(f"  Min SI:  {np.min(lhs_si):.3f}")
print(f"  Max SI:  {np.max(lhs_si):.3f}")
print(f"  Mean SI: {np.mean(lhs_si):.3f}")
print(f"  Wells with SI > 0 (supersaturated): {np.sum(lhs_si > 0)}")
print(f"  Wells with SI < 0 (undersaturated): {np.sum(lhs_si < 0)}")
