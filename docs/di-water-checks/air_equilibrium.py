#!/usr/bin/env python3
"""What air does to deionized water, and whether it matters for the lead stocks.

Part 1 equilibrates pure water with air at 20 and 25 C and reports pH,
dissolved inorganic carbon (DIC), specific conductance and dissolved O2. It
covers outdoor CO2 (425 ppm) and occupied-room CO2 (1,000 and 2,000 ppm), at
sea level and at BYU (about 1,400 m, where the air pressure is about 0.85 atm).

Part 2 makes 10 mM lead(II) nitrate in that water, closed after mixing, and
reports the saturation indices of the lead carbonates and lead hydroxide.

Databases: phreeqc.dat as bundled with phreeqpython (water, CO2, O2,
conductance) and the USGS wateq4f.dat (lead), downloaded at run time; its
sha256 is printed with the results.

Usage:
    pip install phreeqpython
    python docs/di-water-checks/air_equilibrium.py > docs/di-water-checks/results.txt
"""
from __future__ import annotations

import hashlib
import tempfile
import urllib.request
from pathlib import Path

import phreeqpython
from phreeqpython.viphreeqc import VIPhreeqc

PHREEQC_DAT = Path(phreeqpython.__file__).parent / "database" / "phreeqc.dat"
WATEQ4F_URL = "https://raw.githubusercontent.com/usgs-coupled/phreeqc3/master/database/wateq4f.dat"

O2_FRACTION = 0.20946  # dry air
PRESSURE_ATM = {"sea level": 1.0, "BYU, ~1,400 m": 0.845}  # standard atmosphere at 1,400 m
WATER_VAPOUR_ATM = {20: 0.0231, 25: 0.0313}  # saturation vapour pressure
CO2_PPM = (425, 1000, 2000)


def engine(db: Path) -> VIPhreeqc:
    ip = VIPhreeqc()
    ip.load_database(str(db))
    if ip.phc_database_error_count:
        raise RuntimeError(ip.get_error_string()[:500])
    return ip


def run(ip: VIPhreeqc, text: str) -> list[dict]:
    ip.run_string(text)
    if ip.phc_error_count:
        raise RuntimeError(ip.get_error_string()[:500])
    arr = ip.get_selected_output_array()
    return [dict(zip(arr[0], row)) for row in arr[1:]]


def log_p(fraction: float, pressure: float, temp: int) -> float:
    """log10 partial pressure (atm) of a gas in air saturated with water vapour."""
    from math import log10

    return log10(fraction * (pressure - WATER_VAPOUR_ATM[temp]))


def air_equilibrated_water(ip: VIPhreeqc, temp: int, pressure: float, ppm: int) -> dict:
    text = f"""
SOLUTION 1
    temp {temp}
    pH 7 charge
EQUILIBRIUM_PHASES 1
    CO2(g) {log_p(ppm * 1e-6, pressure, temp):.4f} 10
    O2(g)  {log_p(O2_FRACTION, pressure, temp):.4f} 10
SELECTED_OUTPUT 1
    -reset false
    -pH true
USER_PUNCH 1
    -headings SC_uS_cm DIC_umol_kgw O2_mg_kgw
    10 PUNCH SC, TOT("C(4)") * 1e6, TOT("O(0)") * 16000
END
"""
    return run(ip, text)[-1]


def lead_nitrate_stock(ip: VIPhreeqc, dic_mmol: float) -> dict:
    text = f"""
SOLUTION 1
    temp 25
    units mmol/kgw
    pH 7 charge
    Pb    10
    N(5)  20
    C(4)  {dic_mmol:.6g}
SELECTED_OUTPUT 1
    -reset false
    -pH true
    -si Cerussite Hydrocerussite Pb(OH)2
END
"""
    return run(ip, text)[-1]


def main() -> None:
    print("Part 1. Pure water equilibrated with air (phreeqc.dat)")
    print()
    print("| where | T (C) | CO2 (ppm) | pH | DIC (umol/kg) | conductance (uS/cm) | resistivity (MOhm-cm) | O2 (mg/L) |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- |")
    ip = engine(PHREEQC_DAT)
    dic_for_lead = {}
    for where, pressure in PRESSURE_ATM.items():
        for temp in (20, 25):
            for ppm in CO2_PPM:
                r = air_equilibrated_water(ip, temp, pressure, ppm)
                sc = r["SC_uS_cm"]
                print(f"| {where} | {temp} | {ppm} | {r['pH']:.2f} | {r['DIC_umol_kgw']:.1f} | "
                      f"{sc:.2f} | {1 / sc:.2f} | {r['O2_mg_kgw']:.2f} |")
                if temp == 25 and where.startswith("BYU"):
                    dic_for_lead[ppm] = r["DIC_umol_kgw"] / 1000
    pure = run(ip, "SOLUTION 1\n    temp 25\n    pH 7 charge\nSELECTED_OUTPUT 1\n    -reset false\n    -pH true\n"
                   "USER_PUNCH 1\n    -headings SC_uS_cm\n    10 PUNCH SC\nEND\n")[-1]
    print()
    print(f"Pure water with no CO2 at 25 C: pH {pure['pH']:.2f}, {pure['SC_uS_cm']:.3f} uS/cm "
          f"({1 / pure['SC_uS_cm']:.1f} MOhm-cm)")

    print()
    print("Part 2. 10 mM lead(II) nitrate made up in that water, 25 C, BYU (wateq4f.dat)")
    print()
    with tempfile.TemporaryDirectory() as tmp:
        db = Path(tmp) / "wateq4f.dat"
        urllib.request.urlretrieve(WATEQ4F_URL, db)
        print(f"wateq4f.dat sha256 {hashlib.sha256(db.read_bytes()).hexdigest()}")
        print()
        ip = engine(db)
        print("| water's CO2 (ppm) | DIC (umol/kg) | pH | SI cerussite PbCO3 | SI hydrocerussite | SI Pb(OH)2 |")
        print("| --- | --- | --- | --- | --- | --- |")
        for ppm, dic in dic_for_lead.items():
            r = lead_nitrate_stock(ip, dic)
            print(f"| {ppm} | {dic * 1000:.1f} | {r['pH']:.2f} | {r['si_Cerussite']:.2f} | "
                  f"{r['si_Hydrocerussite']:.2f} | {r['si_Pb(OH)2']:.2f} |")
    print()
    print("SI < 0 means undersaturated: that solid cannot form.")


if __name__ == "__main__":
    main()
