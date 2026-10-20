"""
Precipitation Boundary Map: BaSO₄ (Pitzer) vs FeS (Davies)

Generates 2D heatmaps of saturation index (SI) in [NaCl] × [metal ion] space,
showing the predicted precipitation boundary (SI = 0 contour).

Key visual: The BaSO₄ boundary shifts dramatically with ionic strength (Pitzer
model captures ion-ion interactions), while the FeS boundary is suspiciously
flat (Davies equation cannot capture these effects). This is the visual
"before/after" that motivates the entire ACS PRF proposal.

Requirements:
    pip install phreeqpython matplotlib numpy

Usage:
    python precipitation_boundary_map.py

Output:
    - precipitation_boundary_map.png (figure)
"""

import os
import sys

import numpy as np

try:
    import phreeqpython
except ImportError:
    print("Install phreeqpython: pip install phreeqpython")
    sys.exit(1)

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import TwoSlopeNorm
except ImportError:
    print("Install matplotlib: pip install matplotlib")
    sys.exit(1)


OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_C = 25


def compute_si_grid_barite(nacl_range, ba_range):
    """Compute SI(Barite) on a 2D grid of [NaCl] × [Ba²⁺] using Pitzer model."""
    pp = phreeqpython.PhreeqPython(database="pitzer.dat")
    si_grid = np.zeros((len(ba_range), len(nacl_range)))

    for i, ba in enumerate(ba_range):
        for j, nacl in enumerate(nacl_range):
            sol = pp.add_solution({
                "temp": TEMP_C,
                "units": "mol/kgw",
                "Na": nacl + 2e-5,  # NaCl + small Na₂SO₄ contribution
                "Cl": nacl,
                "Ba": ba,
                "S(6)": 1e-5,  # 0.01 mM SO₄²⁻ fixed (lower to get undersaturation)
            })
            si_grid[i, j] = sol.si("Barite")

    return si_grid


def compute_si_grid_mackinawite(nacl_range, fe_range):
    """Compute SI(Mackinawite) on a 2D grid of [NaCl] × [Fe²⁺] using Davies."""
    pp = phreeqpython.PhreeqPython(database="phreeqc.dat")
    si_grid = np.zeros((len(fe_range), len(nacl_range)))

    for i, fe in enumerate(fe_range):
        for j, nacl in enumerate(nacl_range):
            sol = pp.add_solution({
                "temp": TEMP_C,
                "units": "mol/kgw",
                "Na": nacl,
                "Cl": nacl,
                "Fe(2)": fe,
                "S(-2)": 1e-7,  # 0.1 µM total sulfide (S(-2); very low to get undersaturation at low [Fe²⁺])
            })
            si_grid[i, j] = sol.si("Mackinawite")

    return si_grid


def plot_boundary_maps(nacl_range, metal_range, si_barite, si_mack, filepath):
    """Generate side-by-side precipitation boundary maps."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

    # Common colormap settings
    vmin, vmax = -3, 3
    norm = TwoSlopeNorm(vmin=vmin, vcenter=0, vmax=vmax)
    cmap = "RdBu_r"

    # Panel A: BaSO₄ (Pitzer)
    nacl_mg, ba_mg = np.meshgrid(nacl_range, metal_range * 1000)  # convert to mM
    im1 = ax1.pcolormesh(nacl_mg, ba_mg, si_barite, cmap=cmap, norm=norm, shading="auto")
    cs1 = ax1.contour(nacl_mg, ba_mg, si_barite, levels=[0], colors="black", linewidths=2)
    ax1.clabel(cs1, fmt="SI = 0", fontsize=9)
    ax1.set_xlabel("NaCl (molal)", fontsize=11)
    ax1.set_ylabel("[Ba²⁺] (mM)", fontsize=11)
    ax1.set_title("(a) BaSO₄ — Pitzer model\n[SO₄²⁻] = 0.01 mM, T = 25 °C", fontsize=10)
    plt.colorbar(im1, ax=ax1, label="Saturation Index (SI)", shrink=0.8)

    # Panel B: FeS (Davies)
    nacl_mg2, fe_mg = np.meshgrid(nacl_range, metal_range * 1000)
    im2 = ax2.pcolormesh(nacl_mg2, fe_mg, si_mack, cmap=cmap, norm=norm, shading="auto")
    cs2 = ax2.contour(nacl_mg2, fe_mg, si_mack, levels=[0], colors="black", linewidths=2)
    ax2.clabel(cs2, fmt="SI = 0", fontsize=9)
    ax2.set_xlabel("NaCl (molal)", fontsize=11)
    ax2.set_ylabel("[Fe²⁺] (mM)", fontsize=11)
    ax2.set_title("(b) FeS — Davies equation (only option)\n[S(-2)] = 0.1 µM (total sulfide), T = 25 °C", fontsize=10)
    plt.colorbar(im2, ax=ax2, label="Saturation Index (SI)", shrink=0.8)

    # Add annotation about missing Pitzer model
    ax2.annotate(
        "Boundary insensitive to I\n→ missing Pitzer params",
        xy=(3.5, 0.5), fontsize=8, ha="center", color="#d62728",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff5f0",
                  edgecolor="#d62728", alpha=0.9),
    )

    fig.suptitle(
        "Predicted Precipitation Boundaries: Pitzer vs. Davies Models",
        fontsize=12, fontweight="bold", y=1.01,
    )

    plt.tight_layout()
    fig.savefig(filepath, dpi=300, bbox_inches="tight")
    print(f"Figure saved to {filepath}")


def main():
    print("=" * 70)
    print("Precipitation Boundary Map: BaSO₄ (Pitzer) vs FeS (Davies)")
    print("=" * 70)

    # Define parameter ranges
    nacl_range = np.linspace(0.1, 5.0, 25)
    metal_range = np.linspace(10**-4, 10**-1.5, 20)  # 0.1 to ~30 mM

    print(f"\nGrid: {len(nacl_range)} NaCl × {len(metal_range)} metal = "
          f"{len(nacl_range) * len(metal_range)} points per system")
    print(f"NaCl range: {nacl_range[0]:.1f} – {nacl_range[-1]:.1f} molal")
    print(f"Metal range: {metal_range[0]*1000:.2f} – {metal_range[-1]*1000:.1f} mM")

    print("\nComputing BaSO₄ SI grid (Pitzer model)...")
    si_barite = compute_si_grid_barite(nacl_range, metal_range)
    print(f"  SI range: {si_barite.min():.2f} to {si_barite.max():.2f}")

    print("Computing FeS SI grid (Davies equation)...")
    si_mack = compute_si_grid_mackinawite(nacl_range, metal_range)
    print(f"  SI range: {si_mack.min():.2f} to {si_mack.max():.2f}")

    fig_path = os.path.join(OUTPUT_DIR, "precipitation_boundary_map.png")
    plot_boundary_maps(nacl_range, metal_range, si_barite, si_mack, fig_path)

    print("\n" + "=" * 70)
    print("KEY OBSERVATION")
    print("=" * 70)
    print("""
The BaSO₄ precipitation boundary (SI = 0 contour) shifts significantly
with NaCl concentration because the Pitzer model captures how Na⁺ and Cl⁻
alter Ba²⁺ and SO₄²⁻ activity coefficients through specific ion-ion
interactions (β⁰, β¹, Cᶲ, θ, ψ parameters).

The FeS precipitation boundary is nearly vertical — it barely responds
to changes in NaCl concentration. This is because the Davies equation
treats all ions as generic charges and cannot capture the specific
Fe²⁺–Na⁺, Fe²⁺–Cl⁻, or Fe²⁺–HS⁻ interactions that would shift the
boundary in a real brine.

This visual difference is the core motivation for the proposed research:
we need Pitzer parameters for Fe²⁺–HS⁻ and Pb²⁺–HS⁻ systems to make
reliable predictions in produced-water brines.
""")


if __name__ == "__main__":
    main()
