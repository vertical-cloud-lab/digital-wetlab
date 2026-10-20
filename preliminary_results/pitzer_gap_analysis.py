"""
Pitzer-Model Gap Analysis for Sulfide Scales in Produced-Water Brines

Computes saturation indices (SI) for BaSO4 (barite) and FeS (mackinawite)
across produced-water-relevant ionic strengths using PHREEQC via phreeqpython.

Key finding: The standard Pitzer database (pitzer.dat) includes validated
interaction parameters for Ba2+-SO42- but LACKS parameters for Fe2+-HS- and
has no Pb2+ species at all. This means sulfide-scale predictions in high-
ionic-strength brines (I > 1 m) rely on the Davies equation, which is
unreliable above I ~ 0.5 m.

An Edison Scientific literature search (2026-02-28) confirmed that no
published Pitzer parameters exist for Fe2+-HS-, Pb2+-HS-, or related
mixing parameters. HS- interactions with major cations (Na+, K+, Mg2+,
Ca2+) are parameterized (Millero 1986), and Pb2+ in chloride brines is
modeled (Felmy et al. 2000), but no metal-sulfide cross-interactions exist.

This script generates data for Figure 1 of the ACS PRF DNI proposal.

Requirements:
    pip install phreeqpython matplotlib

Usage:
    python pitzer_gap_analysis.py

Output:
    - pitzer_gap_analysis.png (figure)
    - pitzer_gap_analysis.csv (data table)

References:
    - Parkhurst & Appelo (2013), USGS Techniques and Methods 6-A43
    - Kan et al. (2019), SPE J., doi:10.2118/190754-pa
    - Wang et al. (2020), SPE, doi:10.2118/200699-ms
    - Millero (1986), Marine Chemistry, doi:10.1016/0304-4203(86)90003-4
    - Felmy et al. (2000), GCA, doi:10.1016/s0016-7037(00)00454-3
"""

import csv
import os
import sys

try:
    import phreeqpython
except ImportError:
    print("Install phreeqpython: pip install phreeqpython")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
NACL_MOLAL = [0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0]
BA_MOLAL = 0.001   # 1 mmol/kg Ba2+
SO4_MOLAL = 0.001  # 1 mmol/kg SO42-
FE_MOLAL = 0.001   # 1 mmol/kg Fe2+
S2_MOLAL = 0.001   # 1 mmol/kg S(-2) (sulfide)
TEMP_C = 25

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

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
        results.append({
            "NaCl_m": nacl,
            "I_m": sol.I,
            "SI_Barite_Pitzer": sol.si("Barite"),
            "model": "Pitzer",
        })
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
        results.append({
            "NaCl_m": nacl,
            "I_m": sol.I,
            "SI_Barite_Davies": sol.si("Barite"),
            "model": "Davies",
        })
    return results


def compute_mackinawite_davies(nacl_values):
    """Compute SI(Mackinawite) using the Davies equation (phreeqc.dat).

    This is the ONLY model available for FeS because the standard Pitzer
    database lacks Fe2+-HS- interaction parameters and Mackinawite phase.
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
        results.append({
            "NaCl_m": nacl,
            "I_m": sol.I,
            "SI_Mackinawite_Davies": sol.si("Mackinawite"),
            "model": "Davies (only option)",
        })
    return results


def compute_barite_temperature(temps, nacl=2.0):
    """Compute SI(Barite) vs temperature at fixed NaCl using Pitzer model."""
    pp = phreeqpython.PhreeqPython(database="pitzer.dat")
    results = []
    for temp in temps:
        sol = pp.add_solution({
            "temp": temp,
            "units": "mol/kgw",
            "Na": nacl,
            "Cl": nacl,
            "Ba": BA_MOLAL,
            "S(6)": SO4_MOLAL,
        })
        results.append({
            "temp_C": temp,
            "SI_Barite_Pitzer": sol.si("Barite"),
            "I_m": sol.I,
        })
    return results


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def print_results(barite_p, barite_d, mack_d):
    """Print comparison table to console."""
    print(f"\n{'NaCl':>6} {'I':>6} {'SI_Barite':>10} {'SI_Barite':>10} "
          f"{'SI_Mack':>10} {'Pitzer-Davies':>14} {'Note':>25}")
    print(f"{'(m)':>6} {'(m)':>6} {'(Pitzer)':>10} {'(Davies)':>10} "
          f"{'(Davies)':>10} {'Δ(Barite)':>14} {'':>25}")
    print("-" * 90)

    for bp, bd, md in zip(barite_p, barite_d, mack_d):
        nacl = bp["NaCl_m"]
        ionic = bp["I_m"]
        si_bp = bp["SI_Barite_Pitzer"]
        si_bd = bd["SI_Barite_Davies"]
        si_md = md["SI_Mackinawite_Davies"]
        delta = si_bp - si_bd
        note = "" if nacl < 1.0 else "← Davies unreliable" if nacl >= 1.5 else ""
        print(f"{nacl:>6.2f} {ionic:>6.2f} {si_bp:>10.4f} {si_bd:>10.4f} "
              f"{si_md:>10.4f} {delta:>+14.4f} {note:>25}")


def write_csv(barite_p, barite_d, mack_d, filepath):
    """Write combined results to CSV."""
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "NaCl_molal", "I_molal",
            "SI_Barite_Pitzer", "SI_Barite_Davies", "SI_Mackinawite_Davies",
            "Delta_Barite_Pitzer_minus_Davies",
        ])
        for bp, bd, md in zip(barite_p, barite_d, mack_d):
            writer.writerow([
                f"{bp['NaCl_m']:.2f}",
                f"{bp['I_m']:.4f}",
                f"{bp['SI_Barite_Pitzer']:.4f}",
                f"{bd['SI_Barite_Davies']:.4f}",
                f"{md['SI_Mackinawite_Davies']:.4f}",
                f"{bp['SI_Barite_Pitzer'] - bd['SI_Barite_Davies']:.4f}",
            ])
    print(f"\nCSV written to {filepath}")


def plot_results(barite_p, barite_d, mack_d, filepath):
    """Generate publication-quality figure if matplotlib is available."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available — skipping figure generation")
        return

    nacl = [r["NaCl_m"] for r in barite_p]
    si_bp = [r["SI_Barite_Pitzer"] for r in barite_p]
    si_bd = [r["SI_Barite_Davies"] for r in barite_d]
    si_md = [r["SI_Mackinawite_Davies"] for r in mack_d]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), sharey=False)

    # Panel A: Barite — Pitzer vs Davies
    ax1.plot(nacl, si_bp, "o-", color="#2171b5", label="BaSO₄ (Pitzer model)", linewidth=2, markersize=5)
    ax1.plot(nacl, si_bd, "s--", color="#6baed6", label="BaSO₄ (Davies equation)", linewidth=1.5, markersize=4)
    ax1.axhline(0, color="gray", linestyle=":", linewidth=0.8)
    ax1.axvspan(1.5, 5.5, alpha=0.08, color="red", label="Davies unreliable (I > 1.5 m)")
    ax1.set_xlabel("NaCl (molal)", fontsize=11)
    ax1.set_ylabel("Saturation Index (SI)", fontsize=11)
    ax1.set_title("(a) BaSO₄ — Pitzer parameters available", fontsize=11)
    ax1.legend(fontsize=8, loc="upper right")
    ax1.set_xlim(0, 5.3)

    # Panel B: Mackinawite — Davies only (no Pitzer available)
    ax2.plot(nacl, si_md, "^-", color="#e6550d", label="FeS (Davies equation — only option)", linewidth=2, markersize=5)
    ax2.axhline(0, color="gray", linestyle=":", linewidth=0.8)
    ax2.axvspan(0.5, 5.5, alpha=0.08, color="red", label="Davies unreliable (I > 0.5 m)")

    # Add annotation about missing Pitzer model
    ax2.annotate(
        "No Pitzer model available\nfor Fe²⁺–HS⁻ system\n(missing θ, ψ parameters)",
        xy=(3.0, 2.5), fontsize=9, ha="center",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#fee0d2", edgecolor="#e6550d", alpha=0.9),
    )

    ax2.set_xlabel("NaCl (molal)", fontsize=11)
    ax2.set_ylabel("Saturation Index (SI)", fontsize=11)
    ax2.set_title("(b) FeS — No Pitzer parameters", fontsize=11)
    ax2.legend(fontsize=8, loc="lower right")
    ax2.set_xlim(0, 5.3)

    fig.suptitle(
        "Thermodynamic Model Gap: Sulfate vs. Sulfide Scale Predictions\n"
        f"[Ba²⁺] = [Fe²⁺] = {BA_MOLAL*1000:.0f} mM, "
        f"[SO₄²⁻] = {SO4_MOLAL*1000:.0f} mM, total sulfide (S(-II)) = {S2_MOLAL*1000:.0f} mM, T = {TEMP_C} °C",
        fontsize=12, fontweight="bold", y=1.02,
    )

    plt.tight_layout()
    fig.savefig(filepath, dpi=300, bbox_inches="tight")
    print(f"Figure saved to {filepath}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("Pitzer-Model Gap Analysis for Sulfide Scales")
    print("=" * 70)

    print("\nDatabase contents summary:")
    print("  pitzer.dat: Ba²⁺ ✅  Fe²⁺ (Cl⁻, SO₄²⁻ only) ⚠️  Pb²⁺ ❌")
    print("  pitzer.dat: Barite ✅  Mackinawite ❌  Galena ❌")
    print("  phreeqc.dat: Mackinawite ✅  (but uses Davies equation)")
    print()

    # Compute
    barite_p = compute_barite_pitzer(NACL_MOLAL)
    barite_d = compute_barite_davies(NACL_MOLAL)
    mack_d = compute_mackinawite_davies(NACL_MOLAL)

    # Print
    print_results(barite_p, barite_d, mack_d)

    # Temperature dependence
    temps = [25, 40, 60, 80, 90]
    temp_results = compute_barite_temperature(temps)
    print(f"\nBarite SI vs temperature (NaCl = 2.0 m, Pitzer model):")
    for r in temp_results:
        print(f"  {r['temp_C']:>3d} °C: SI = {r['SI_Barite_Pitzer']:.4f}")

    # Write outputs
    csv_path = os.path.join(OUTPUT_DIR, "pitzer_gap_analysis.csv")
    fig_path = os.path.join(OUTPUT_DIR, "pitzer_gap_analysis.png")

    write_csv(barite_p, barite_d, mack_d, csv_path)
    plot_results(barite_p, barite_d, mack_d, fig_path)

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY: Why this matters for the ACS PRF proposal")
    print("=" * 70)
    print("""
For BaSO₄ (barite), the Pitzer model provides reliable saturation index
predictions across the full produced-water ionic strength range (0.1–5+ m).
This is because Ba²⁺–Na⁺, Ba²⁺–Cl⁻, SO₄²⁻–Na⁺, and related interaction
parameters are well-characterized in the literature (Kan et al. 2019).

For FeS (mackinawite) and PbS (galena), NO Pitzer model is available:
  - Fe²⁺ has Pitzer parameters only for Cl⁻ and SO₄²⁻ (not HS⁻)
  - Pb²⁺ is entirely absent from the standard Pitzer database
  - Neither Mackinawite nor Galena phases are defined in pitzer.dat
  - The only available model (Davies equation) is unreliable above I ≈ 0.5 m

Edison Scientific literature search (2026-02-28) confirmed:
  - HS⁻ parameters with major cations exist (Millero 1986)
  - Pb²⁺–Cl⁻ brine parameters exist (Felmy et al. 2000)
  - NO Fe²⁺–HS⁻ or Pb²⁺–HS⁻ Pitzer parameters have been published
  - NO higher-order mixing (θ, ψ) parameters for sulfide systems exist

The proposal targets 14 specific missing parameters:
  - 6 binary (β⁰, β¹, Cᶲ for Fe²⁺–HS⁻ and Pb²⁺–HS⁻)
  - 8 mixing (θ and ψ for Fe²⁺/Pb²⁺ with Na⁺ and Ca²⁺)
""")


if __name__ == "__main__":
    main()
