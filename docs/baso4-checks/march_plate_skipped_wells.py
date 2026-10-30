"""Which wells of the 03-05 BaSO4 plate got no barium, sulfate or NaCl.

The protocol that ran (commit cded249, Experiment_1__AgCl_Precipitation_V1.py) sets any
volume under 1 uL, the P20's minimum, to zero. With 1 M barium chloride and sodium sulfate
stocks and 200 uL wells, that drops every dose under 5 mM. This re-runs that rule on the
protocol's own 80-condition list.

Run from the repo root:  python docs/baso4-checks/march_plate_skipped_wells.py
"""
import re
import subprocess

SRC = subprocess.run(
    ["git", "show", "cded249:Experiment_1__AgCl_Precipitation_V1.py"],
    capture_output=True, text=True, check=True,
).stdout

ROWS = re.findall(
    r"\(\s*([\d.]+),\s*([\d.]+),\s*([\d.]+)\),\s*#\s*Well\s+\d+\s+\((\w+)\)", SRC)
assert len(ROWS) == 80, len(ROWS)

STOCK = {"barium chloride": 1000.0, "sodium sulfate": 1000.0, "NaCl": 5.0}  # mM, mM, M
TOTAL_UL, MIN_UL = 200.0, 1.0

skipped = {k: [] for k in STOCK}
under_2 = []
for ba, so4, nacl, well in ROWS:
    for name, conc in zip(STOCK, (float(ba), float(so4), float(nacl))):
        ul = conc / STOCK[name] * TOTAL_UL
        if ul < MIN_UL:
            skipped[name].append(f"{well} ({conc:g} -> {ul:.2f} uL)")
        elif ul < 2 and name != "NaCl":
            under_2.append(f"{well} {name} {ul:.2f} uL")

for name, wells in skipped.items():
    print(f"No {name} dispensed: {len(wells)} of 80 conditions")
    for w in wells:
        print(f"  {w}")
print(f"\nDispensed, but under 2 uL (the P20 is least accurate there): {len(under_2)}")
for w in under_2:
    print(f"  {w}")
