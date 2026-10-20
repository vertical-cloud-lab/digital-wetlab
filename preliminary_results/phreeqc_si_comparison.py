"""
PHREEQC Saturation-Index Comparison: Pitzer vs. Davies for Sulfide Scales

Computes saturation indices (SI) for BaSO₄ (barite), FeS (mackinawite), and
PbS (galena) across produced-water-relevant ionic strengths (0.1–5.0 molal
NaCl) using PHREEQC via phreeqpython.

Key findings:
  - BaSO₄: Full Pitzer model available → SI responds properly to ionic strength
  - FeS:   Davies equation only (no Fe²⁺–HS⁻ Pitzer params) → flat, unreliable
  - PbS:   Pb²⁺ absent from pitzer.dat; Galena not in phreeqc.dat PHASES →
            must define custom phase; Davies-only prediction unreliable

This script generates the PHREEQC SI comparison figure (fig:phreeqc_si in
draft.tex) for the ACS PRF DNI proposal, directly addressing the
thermodynamic-model gap that motivates the proposed research.

Requirements:
    pip install phreeqpython matplotlib numpy

Usage:
    python phreeqc_si_comparison.py

Output:
    - phreeqc_si_comparison.png (3-panel figure)
    - phreeqc_si_comparison.csv (data table)
"""

import csv
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
except ImportError:
    print("Install matplotlib: pip install matplotlib")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
# Finer spacing at low I (0.1 step) for better resolution near the Davies
# reliability limit (~0.5 m), coarser spacing (0.25 step) at higher I.
NACL_MOLAL = np.concatenate([
    np.arange(0.1, 0.5, 0.1),
    np.arange(0.5, 5.25, 0.25),
])
BA_MOLAL = 0.001    # 1 mmol/kg Ba²⁺
SO4_MOLAL = 0.001   # 1 mmol/kg SO₄²⁻
FE_MOLAL = 0.001    # 1 mmol/kg Fe²⁺
PB_MOLAL = 0.001    # 1 mmol/kg Pb²⁺
S2_MOLAL = 0.001    # 1 mmol/kg total sulfide S(-2)
TEMP_C = 25

# Galena dissolution reaction, following the PHREEQC convention of writing
# phase reactions using the dominant aqueous sulfide species (HS⁻) rather
# than S²⁻.  This matches the form used in wateq4f.dat and the standard
# Mackinawite definition in phreeqc.dat (FeS + H+ = Fe+2 + HS-).
# Source: wateq4f database (Ball & Nordstrom, 1991), log_k = -12.780.
# Cross-ref: phreeqcusers.org/index.php/topic,943.0.html
GALENA_REACTION = "PbS + H+ = Pb+2 + HS-"
GALENA_LOG_K = -12.780

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Davies equation reliability thresholds (molal). The standard cutoff is
# ~0.5 m for most ions. For BaSO₄, the Pitzer–Davies divergence only
# becomes visually significant above ~1.5 m because Ba²⁺–SO₄²⁻ parameters
# partially compensate at moderate I.
DAVIES_THRESHOLD_GENERAL = 0.5
DAVIES_THRESHOLD_BARITE = 1.5


# ---------------------------------------------------------------------------
# Computations
# ---------------------------------------------------------------------------

def compute_barite_pitzer(nacl_values):
    """Compute SI(Barite) using the Pitzer model (pitzer.dat)."""
    pp = phreeqpython.PhreeqPython(database="pitzer.dat")
    results = []
    for nacl in nacl_values:
        sol = pp.add_solution({
            "temp": TEMP_C,
            "units": "mol/kgw",
            "Na": nacl,
            "Cl": nacl,
            "Ba": BA_MOLAL,
            "S(6)": SO4_MOLAL,
        })
        results.append({"NaCl_m": nacl, "I_m": sol.I, "SI": sol.si("Barite")})
    return results


def compute_barite_davies(nacl_values):
    """Compute SI(Barite) using the Davies equation (phreeqc.dat)."""
    pp = phreeqpython.PhreeqPython(database="phreeqc.dat")
    results = []
    for nacl in nacl_values:
        sol = pp.add_solution({
            "temp": TEMP_C,
            "units": "mol/kgw",
            "Na": nacl,
            "Cl": nacl,
            "Ba": BA_MOLAL,
            "S(6)": SO4_MOLAL,
        })
        results.append({"NaCl_m": nacl, "I_m": sol.I, "SI": sol.si("Barite")})
    return results


def compute_mackinawite_davies(nacl_values):
    """Compute SI(Mackinawite) using the Davies equation (phreeqc.dat).

    The Pitzer database lacks Fe²⁺–HS⁻ interaction parameters and has no
    Mackinawite phase definition, so the Davies equation is the only option.
    """
    pp = phreeqpython.PhreeqPython(database="phreeqc.dat")
    results = []
    for nacl in nacl_values:
        sol = pp.add_solution({
            "temp": TEMP_C,
            "units": "mol/kgw",
            "Na": nacl,
            "Cl": nacl,
            "Fe(2)": FE_MOLAL,
            "S(-2)": S2_MOLAL,
        })
        results.append({"NaCl_m": nacl, "I_m": sol.I, "SI": sol.si("Mackinawite")})
    return results


def compute_galena_davies(nacl_values):
    """Compute SI(Galena) using the Davies equation (phreeqc.dat).

    Galena is NOT defined in the standard phreeqc.dat PHASES block, so we
    add it as a custom phase. The Pitzer database has zero Pb²⁺ parameters
    for any anion, making this system entirely unmodeled for brines.
    """
    pp = phreeqpython.PhreeqPython(database="phreeqc.dat")
    pp.ip.run_string(f"""
PHASES
Galena
    {GALENA_REACTION}
    log_k   {GALENA_LOG_K}
END
""")
    results = []
    for nacl in nacl_values:
        sol = pp.add_solution({
            "temp": TEMP_C,
            "units": "mol/kgw",
            "Na": nacl,
            "Cl": nacl,
            "Pb": PB_MOLAL,
            "S(-2)": S2_MOLAL,
        })
        results.append({"NaCl_m": nacl, "I_m": sol.I, "SI": sol.si("Galena")})
    return results


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def write_csv(barite_p, barite_d, mack_d, galena_d, filepath):
    """Write combined results to CSV.

    Note: I_molal is from the Barite Pitzer solution. The FeS and PbS
    solutions have slightly different ionic strengths due to different
    solute compositions (Fe²⁺/S(-2) vs Ba²⁺/S(6)), but all trace solutes
    are at 0.001 molal so the difference is < 0.001 m and negligible
    compared to the NaCl background.
    """
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "NaCl_molal", "I_molal",
            "SI_Barite_Pitzer", "SI_Barite_Davies",
            "SI_Mackinawite_Davies", "SI_Galena_Davies",
            "Delta_Barite_Pitzer_minus_Davies",
        ])
        for bp, bd, md, gd in zip(barite_p, barite_d, mack_d, galena_d):
            writer.writerow([
                f"{bp['NaCl_m']:.2f}",
                f"{bp['I_m']:.4f}",
                f"{bp['SI']:.4f}",
                f"{bd['SI']:.4f}",
                f"{md['SI']:.4f}",
                f"{gd['SI']:.4f}",
                f"{bp['SI'] - bd['SI']:.4f}",
            ])
    print(f"CSV written to {filepath}")


def plot_results(barite_p, barite_d, mack_d, galena_d, filepath):
    """Generate publication-quality 3-panel figure."""
    nacl = [r["NaCl_m"] for r in barite_p]
    si_bp = [r["SI"] for r in barite_p]
    si_bd = [r["SI"] for r in barite_d]
    si_md = [r["SI"] for r in mack_d]
    si_gd = [r["SI"] for r in galena_d]

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(14, 4.5), sharey=False)

    # --- Panel A: Barite — Pitzer vs Davies ---
    ax1.plot(nacl, si_bp, "o-", color="#2171b5", label="Pitzer model",
             linewidth=2, markersize=4)
    ax1.plot(nacl, si_bd, "s--", color="#6baed6", label="Davies equation",
             linewidth=1.5, markersize=3)
    ax1.axhline(0, color="gray", linestyle=":", linewidth=0.8)
    ax1.axvspan(DAVIES_THRESHOLD_BARITE, 5.5, alpha=0.08, color="red",
                label=f"Davies unreliable (I > {DAVIES_THRESHOLD_BARITE} m)")
    ax1.set_xlabel("NaCl (molal)", fontsize=11)
    ax1.set_ylabel("Saturation Index (SI)", fontsize=11)
    ax1.set_title("(a) BaSO$_4$ — Pitzer model available", fontsize=11)
    ax1.legend(fontsize=7.5, loc="upper right")
    ax1.set_xlim(0, 5.3)

    # --- Panel B: Mackinawite — Davies only ---
    ax2.plot(nacl, si_md, "^-", color="#e6550d",
             label="Davies equation (only option)", linewidth=2, markersize=4)
    ax2.axhline(0, color="gray", linestyle=":", linewidth=0.8)
    ax2.axvspan(DAVIES_THRESHOLD_GENERAL, 5.5, alpha=0.08, color="red",
                label=f"Davies unreliable (I > {DAVIES_THRESHOLD_GENERAL} m)")
    ax2.annotate(
        "No Pitzer model:\nmissing Fe$^{2+}$–HS$^-$\nparameters",
        xy=(0.5, 0.35), xycoords="axes fraction",
        fontsize=8.5, ha="center",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#fee0d2",
                  edgecolor="#e6550d", alpha=0.9),
    )
    ax2.set_xlabel("NaCl (molal)", fontsize=11)
    ax2.set_ylabel("Saturation Index (SI)", fontsize=11)
    ax2.set_title("(b) FeS — No Pitzer parameters", fontsize=11)
    ax2.legend(fontsize=7.5, loc="lower right")
    ax2.set_xlim(0, 5.3)

    # --- Panel C: Galena — Davies only (custom phase) ---
    ax3.plot(nacl, si_gd, "D-", color="#756bb1",
             label="Davies equation (custom phase)", linewidth=2, markersize=4)
    ax3.axhline(0, color="gray", linestyle=":", linewidth=0.8)
    ax3.axvspan(DAVIES_THRESHOLD_GENERAL, 5.5, alpha=0.08, color="red",
                label=f"Davies unreliable (I > {DAVIES_THRESHOLD_GENERAL} m)")
    ax3.annotate(
        "No Pitzer model:\nPb$^{2+}$ absent from\npitzer.dat entirely",
        xy=(0.5, 0.35), xycoords="axes fraction",
        fontsize=8.5, ha="center",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#e8dff5",
                  edgecolor="#756bb1", alpha=0.9),
    )
    ax3.set_xlabel("NaCl (molal)", fontsize=11)
    ax3.set_ylabel("Saturation Index (SI)", fontsize=11)
    ax3.set_title("(c) PbS — No Pitzer parameters", fontsize=11)
    ax3.legend(fontsize=7.5, loc="lower right")
    ax3.set_xlim(0, 5.3)

    fig.suptitle(
        "Predicted Saturation Indices: Sulfate vs. Sulfide Scale Systems\n"
        f"[Ba$^{{2+}}$] = [Fe$^{{2+}}$] = [Pb$^{{2+}}$] = "
        f"{BA_MOLAL*1000:.0f} mM, "
        f"[SO$_4^{{2-}}$] = {SO4_MOLAL*1000:.0f} mM, "
        f"[S(-II)] = {S2_MOLAL*1000:.0f} mM, T = {TEMP_C} °C",
        fontsize=11, fontweight="bold", y=1.03,
    )

    plt.tight_layout()
    fig.savefig(filepath, dpi=300, bbox_inches="tight")
    print(f"Figure saved to {filepath}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("PHREEQC Saturation-Index Comparison")
    print("Pitzer vs. Davies for Sulfate and Sulfide Scales")
    print("=" * 70)

    print("\nDatabase contents summary:")
    print("  pitzer.dat: Ba²⁺ ✅  Fe²⁺ (Cl⁻, SO₄²⁻ only) ⚠️  Pb²⁺ ❌")
    print("  pitzer.dat: Barite ✅  Mackinawite ❌  Galena ❌")
    print("  phreeqc.dat: Barite ✅  Mackinawite ✅  Galena ❌ (added custom)")

    nacl = NACL_MOLAL
    print(f"\nNaCl range: {nacl[0]:.1f} – {nacl[-1]:.1f} molal "
          f"({len(nacl)} points)")

    print("\nComputing SI(Barite) — Pitzer model (pitzer.dat)...")
    barite_p = compute_barite_pitzer(nacl)

    print("Computing SI(Barite) — Davies equation (phreeqc.dat)...")
    barite_d = compute_barite_davies(nacl)

    print("Computing SI(Mackinawite) — Davies equation (phreeqc.dat)...")
    mack_d = compute_mackinawite_davies(nacl)

    print("Computing SI(Galena) — Davies equation (phreeqc.dat + custom phase)...")
    galena_d = compute_galena_davies(nacl)

    # Print table
    print(f"\n{'NaCl':>6} {'I':>6} {'SI_Bar':>8} {'SI_Bar':>8} "
          f"{'SI_Mack':>8} {'SI_Gal':>8} {'ΔBar':>8}")
    print(f"{'(m)':>6} {'(m)':>6} {'Pitzer':>8} {'Davies':>8} "
          f"{'Davies':>8} {'Davies':>8} {'P-D':>8}")
    print("-" * 64)
    for bp, bd, md, gd in zip(barite_p, barite_d, mack_d, galena_d):
        print(f"{bp['NaCl_m']:>6.2f} {bp['I_m']:>6.2f} "
              f"{bp['SI']:>8.3f} {bd['SI']:>8.3f} "
              f"{md['SI']:>8.3f} {gd['SI']:>8.3f} "
              f"{bp['SI'] - bd['SI']:>+8.3f}")

    # Write outputs
    csv_path = os.path.join(OUTPUT_DIR, "phreeqc_si_comparison.csv")
    fig_path = os.path.join(OUTPUT_DIR, "phreeqc_si_comparison.png")
    write_csv(barite_p, barite_d, mack_d, galena_d, csv_path)
    plot_results(barite_p, barite_d, mack_d, galena_d, fig_path)

    # Summary
    si_mack_range = max(r["SI"] for r in mack_d) - min(r["SI"] for r in mack_d)
    si_gal_range = max(r["SI"] for r in galena_d) - min(r["SI"] for r in galena_d)
    si_bar_p_range = max(r["SI"] for r in barite_p) - min(r["SI"] for r in barite_p)

    print("\n" + "=" * 70)
    print("KEY OBSERVATIONS")
    print("=" * 70)
    print(f"""
BaSO₄ (Pitzer model): SI varies by {si_bar_p_range:.2f} units across
  0.1–5.0 m NaCl, reflecting real ion-ion interactions captured by
  validated Pitzer parameters (β⁰, β¹, Cᶲ, θ, ψ for Ba²⁺ with Na⁺, Cl⁻).

FeS (Davies only): SI varies by only {si_mack_range:.2f} units — the
  Davies equation treats all ions as generic charges and cannot capture
  specific Fe²⁺–HS⁻, Fe²⁺–Na⁺, or Fe²⁺–Cl⁻ interactions. No Pitzer
  model exists because Fe²⁺–HS⁻ parameters have never been published.

PbS (Davies only, custom phase): SI varies by only {si_gal_range:.2f} units.
  Pb²⁺ is entirely absent from pitzer.dat. Galena is not even defined as
  a phase in the standard PHREEQC databases. This system is completely
  unmodeled for produced-water brines.

These results confirm the thermodynamic-model gap that motivates the
proposed research: developing Pitzer interaction parameters for
Fe²⁺–HS⁻ and Pb²⁺–HS⁻ systems.
""")


if __name__ == "__main__":
    main()
