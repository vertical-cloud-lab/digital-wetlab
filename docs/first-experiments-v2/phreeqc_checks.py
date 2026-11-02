"""PHREEQC numbers behind docs/first-experiments-v2/README.md.

1. Barite (BaSO4) supersaturation for the replicate-well induction-time plates: equal barium
   and sulfate, in water and in 1 molal NaCl, at 25 C (deck) and 40, 60, 80 C (heater-shaker).
2. Gypsum (CaSO4.2H2O) solubility in NaCl at 25 C, for the solubility-from-both-sides plate,
   and the supersaturation of equal Ca and SO4 levels in water for gypsum induction times.

PHREEQC with pitzer.dat (IPhreeqc 3.7.3 bundled with phreeqpython 1.6.2), mmol/kgw, pH 7 by
charge balance. Concentrations in a 200 uL well are treated as mmol/kgw; above about 1 molal
NaCl, molar and molal differ by a few per cent, which does not change any conclusion here.
S is the supersaturation ratio for a 1:1 salt, S = (IAP/Ksp)^(1/2) = 10^(SI/2).

Run:  pip install phreeqpython==1.6.2
      python docs/first-experiments-v2/phreeqc_checks.py > docs/first-experiments-v2/results.txt
"""
import math
from pathlib import Path

import phreeqpython
from phreeqpython.viphreeqc import VIPhreeqc

ip = VIPhreeqc()
ip.load_database(str(Path(phreeqpython.__file__).parent / "database" / "pitzer.dat"))

WELL_UL = 200.0
G_PER_MOL = {"Barite": 233.39, "Gypsum": 172.17}


def si(phase, metal, metal_mm, so4_mm, nacl_m, temp_c=25.0):
    """Saturation index of `phase` for metal chloride + sodium sulfate in NaCl."""
    na = 2 * so4_mm + 1000 * nacl_m
    cl = 2 * metal_mm + 1000 * nacl_m
    ip.run_string(f"""SOLUTION 1
    temp {temp_c}
    units mmol/kgw
    pH 7 charge
    {metal} {metal_mm}
    S(6) {so4_mm}
    Na {max(na, 1e-9)}
    Cl {max(cl, 1e-9)}
SELECTED_OUTPUT
    -reset false
    -si {phase}
END
""")
    return float(ip.get_selected_output_array()[1][0])


def solubility_mm(phase, metal, nacl_m, temp_c=25.0):
    """Equal metal and sulfate (mmol/kgw) at which SI = 0, by bisection."""
    lo, hi = 1e-4, 2000.0
    for _ in range(70):
        mid = math.sqrt(lo * hi)
        if si(phase, metal, mid, mid, nacl_m, temp_c) > 0:
            hi = mid
        else:
            lo = mid
    return math.sqrt(lo * hi)


def ug_per_well(phase, mm):
    return mm * 1e-3 * WELL_UL * 1e-6 * G_PER_MOL[phase] * 1e6


# 1. Barite --------------------------------------------------------------------------------
print("1. BARITE, equal barium chloride and sodium sulfate")
print("\nSolubility (equal Ba and SO4 at SI = 0), umol/kgw:")
print("  NaCl (m)   25 C    40 C    60 C    80 C")
for nacl in (0.0, 1.0, 2.0):
    row = [solubility_mm("Barite", "Ba", nacl, t) * 1000 for t in (25, 40, 60, 80)]
    print(f"  {nacl:>7.1f} " + "".join(f"{v:8.0f}" for v in row))

LEVELS_BA = [0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 2.0]
for nacl in (0.0, 1.0):
    print(f"\nSI (and S) for equal Ba = SO4, {nacl:.0f} molal NaCl")
    print("  mM each  ug BaSO4/well   25 C          40 C          60 C          80 C")
    for c in LEVELS_BA:
        cells = []
        for t in (25, 40, 60, 80):
            s_i = si("Barite", "Ba", c, c, nacl, t)
            cells.append(f"{s_i:5.2f} (S {10 ** (s_i / 2):5.1f})")
        print(f"  {c:>7.2f} {ug_per_well('Barite', c):10.1f}     " + " ".join(cells))

# 2. Gypsum --------------------------------------------------------------------------------
print("\n\n2. GYPSUM, equal calcium chloride and sodium sulfate")
print("\nSolubility at 25 C (equal Ca and SO4 at gypsum SI = 0), mmol/kgw, with the anhydrite SI")
print("of that solution (anhydrite is the stable phase where its SI > 0, but it rarely nucleates")
print("below about 100 C):")
print("  NaCl (m)   mmol/kgw   g CaSO4/kg water   anhydrite SI")
for nacl in (0.0, 0.5, 1.0, 2.0, 3.0, 4.0):
    c = solubility_mm("Gypsum", "Ca", nacl, 25)
    anh = si("Anhydrite", "Ca", c, c, nacl, 25)
    print(f"  {nacl:>7.1f} {c:10.1f} {c * 136.14 / 1000:14.2f} {anh:14.2f}")

print("\nGypsum solubility in water against temperature (heater-shaker range), mmol/kgw:")
for t in (25, 40, 60, 80):
    print(f"  {t:>3} C: {solubility_mm('Gypsum', 'Ca', 0.0, t):6.1f}"
          f"   anhydrite SI there {si('Anhydrite', 'Ca', solubility_mm('Gypsum', 'Ca', 0.0, t), solubility_mm('Gypsum', 'Ca', 0.0, t), 0.0, t):5.2f}")

print("\nGypsum SI (and S) for equal Ca = SO4 in water at 25 C (induction-time levels):")
print("  mM each   SI     S     mg gypsum/well if it all came out above solubility")
sol0 = solubility_mm("Gypsum", "Ca", 0.0, 25)
for c in (20, 25, 30, 40, 50, 60, 80):
    s_i = si("Gypsum", "Ca", c, c, 0.0, 25)
    excess_mg = max(c - sol0, 0) * 1e-3 * WELL_UL * 1e-6 * G_PER_MOL["Gypsum"] * 1e3
    print(f"  {c:>7}  {s_i:5.2f}  {10 ** (s_i / 2):5.2f}   {excess_mg:6.2f}")

print("\nBracketing grid for the solubility-from-both-sides plate: total Ca = SO4 as a fraction")
print("of the 25 C solubility at each NaCl level, with the resulting gypsum SI:")
fracs = (0.6, 0.8, 0.9, 1.0, 1.1, 1.25, 1.5)
print("  NaCl (m)  solubility  " + "".join(f"{f:>8.2f}x" for f in fracs))
for nacl in (0.0, 1.0, 2.0):
    sol = solubility_mm("Gypsum", "Ca", nacl, 25)
    sis = [si("Gypsum", "Ca", f * sol, f * sol, nacl, 25) for f in fracs]
    print(f"  {nacl:>7.1f} {sol:9.1f} mM " + "".join(f"{v:9.2f}" for v in sis))


# 3. Matched-SI designs ---------------------------------------------------------------------
def conc_for_si(phase, metal, target_si, nacl_m, temp_c=25.0):
    """Equal metal and sulfate (mmol/kgw) giving `target_si`, by bisection."""
    lo, hi = 1e-4, 2000.0
    for _ in range(70):
        mid = math.sqrt(lo * hi)
        if si(phase, metal, mid, mid, nacl_m, temp_c) > target_si:
            hi = mid
        else:
            lo = mid
    return math.sqrt(lo * hi)


print("\n\n3. MATCHED-SI DESIGNS (equal Ba = SO4)")
print("\nBarite in 1 molal NaCl: mM of each needed for a target SI at each temperature")
print("(for holding SI fixed while the heater-shaker changes T):")
print("  target SI    25 C     40 C     60 C     80 C")
for target in (1.0, 1.5, 2.0, 2.5):
    row = [conc_for_si("Barite", "Ba", target, 1.0, t) for t in (25, 40, 60, 80)]
    print(f"  {target:>9.1f} " + "".join(f"{v:9.2f}" for v in row))

print("\nBarite at 25 C: mM of each for a target SI at each NaCl level, and the most BaSO4 a")
print("200 uL well can then form (the mass a camera has to see differs by this much):")
print("  target SI   NaCl 0 m           1 m                2 m                3 m")
for target in (1.5, 2.0, 2.5):
    cells = []
    for nacl in (0.0, 1.0, 2.0, 3.0):
        c = conc_for_si("Barite", "Ba", target, nacl, 25)
        cells.append(f"{c:5.2f} mM ({ug_per_well('Barite', c):5.1f} ug)")
        
    print(f"  {target:>9.1f}   " + "  ".join(cells))

print("\nE1a range-finding levels: barite in 1 molal NaCl at 25 C. Each well gets 100 uL of a")
print("barium chloride stock and 100 uL of a sodium sulfate stock, each at twice the well value and")
print("both made up in 1 molal NaCl:")
print("  target SI   mM of each in the well   stock (mM)   most BaSO4 per 200 uL well")
for k in range(8):
    target = 1.0 + 0.25 * k
    c = conc_for_si("Barite", "Ba", target, 1.0, 25)
    print(f"  {target:>9.2f} {c:14.2f} {2 * c:17.2f} {ug_per_well('Barite', c):14.1f} ug")
