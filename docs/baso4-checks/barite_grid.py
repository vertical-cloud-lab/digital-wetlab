"""Barite (BaSO4) saturation for the barium sulfate practice plate in the lead plan (step 13).

The plate copies the first lead plate: barium chloride against sodium sulfate at 0.01, 0.1, 1
and 3 mM each, in 1 molal NaCl, plus the same pairs without NaCl and 10 mM + 10 mM positive
controls. PHREEQC with pitzer.dat (IPhreeqc 3.7.3 bundled with phreeqpython 1.6.2), 25 C,
mmol/kgw, pH 7 by charge balance. The mM in a 200 uL well are treated as mmol/kgw.

Run:  pip install phreeqpython==1.6.2
      python docs/baso4-checks/barite_grid.py
"""
import math
from pathlib import Path

import phreeqpython
from phreeqpython.viphreeqc import VIPhreeqc

ip = VIPhreeqc()
ip.load_database(str(Path(phreeqpython.__file__).parent / "database" / "pitzer.dat"))

LEVELS = [0.01, 0.1, 1.0, 3.0]  # mM in the well
BASO4_G_PER_MOL = 233.39
WELL_UL = 200.0


def si_barite(ba_mm, so4_mm, nacl_m):
    na = 2 * so4_mm + 1000 * nacl_m
    cl = 2 * ba_mm + 1000 * nacl_m
    ip.run_string(f"""SOLUTION 1
    temp 25
    units mmol/kgw
    pH 7 charge
    Ba {ba_mm}
    S(6) {so4_mm}
    Na {max(na, 1e-9)}
    Cl {max(cl, 1e-9)}
SELECTED_OUTPUT
    -reset false
    -si Barite
END
""")
    return float(ip.get_selected_output_array()[1][0])


def boundary_mm(nacl_m):
    """Equal Ba and SO4 (mM) at which barite SI = 0."""
    lo, hi = 1e-4, 10.0
    for _ in range(60):
        mid = math.sqrt(lo * hi)
        if si_barite(mid, mid, nacl_m) > 0:
            hi = mid
        else:
            lo = mid
    return math.sqrt(lo * hi)


def grid(nacl_m):
    return {(b, s): si_barite(b, s, nacl_m) for b in LEVELS for s in LEVELS}


def show(table, label):
    print(f"\nBarite SI, {label} (rows: barium mM; columns: sulfate mM)")
    print("Ba \\ SO4 " + "".join(f"{s:>8}" for s in LEVELS))
    for b in LEVELS:
        print(f"{b:>9} " + "".join(f"{table[(b, s)]:8.2f}" for s in LEVELS))


print("Boundary for equal barium and sulfate (SI = 0):")
for n in (0.0, 1.0, 3.0):
    print(f"  {n:.0f} molal NaCl: {boundary_mm(n) * 1000:.0f} uM")

brine, water = grid(1.0), grid(0.0)
show(brine, "1 molal NaCl")
show(water, "no NaCl")

under = sorted(k for k, v in brine.items() if v < -0.1)
near = sorted(k for k, v in brine.items() if -0.1 <= v <= 0.1)
print(f"\n1 molal NaCl: {len(under)} pairs below SI -0.1, {len(near)} within 0.1 of SI 0, "
      f"{16 - len(under) - len(near)} above SI +0.1")
shift = [water[k] - brine[k] for k in brine]
print(f"Removing the NaCl raises SI by {min(shift):.2f} to {max(shift):.2f} units")

print("\nPositive controls, 10 mM barium + 10 mM sulfate:")
print(f"  1 molal NaCl: SI {si_barite(10, 10, 1.0):.2f}")
print(f"  no NaCl:      SI {si_barite(10, 10, 0.0):.2f}")

print("\nMost barium sulfate a 200 uL well can form, set by the scarcer ion:")
for c in LEVELS:
    ug = c * 1e-3 * WELL_UL * 1e-6 * BASO4_G_PER_MOL * 1e6
    print(f"  {c:>5} mM: {ug:.1f} ug")
