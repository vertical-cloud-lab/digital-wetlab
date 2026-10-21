"""PHREEQC saturation-index checks for the OT-2 FeS / PbS brine setup checklist.

All at 25 C, molal units (mol/kg water). Engine: IPhreeqc 3.7.3 bundled with
phreeqpython 1.6.2. Databases: bundled pitzer.dat / phreeqc.dat; llnl.dat,
minteq.v4.dat, wateq4f.dat from usgs-coupled/phreeqc3 (master).
pH is fixed with a Fix_H+ pseudo-phase (H+ = H+, log_k 0) dosing NaOH or HCl
into a charge-balanced starting solution (see pqengine.py).

Run:  pip install phreeqpython==1.6.2
      python docs/phreeqc-checks/phreeqc_checks.py > docs/phreeqc-checks/results.txt
Needs llnl.dat, minteq.v4.dat and wateq4f.dat in a db/ folder next to this
script (see pqengine.py). Writes results.json next to this script.
"""
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from pqengine import Engine, si_val, bisect, mol, la  # noqa: E402

E = {k: Engine(k) for k in ["pitzer", "phreeqc", "llnl", "minteq", "wateq4f"]}
RES = {}
MAX_REAGENT = {"mol": 0.0, "where": ""}


def track(added, where):
    if abs(added) > abs(MAX_REAGENT["mol"]):
        MAX_REAGENT.update(mol=added, where=where)


def f2(x):
    return "  n/a" if x is None else f"{x:5.2f}"


# ----------------------------------------------------------------------------
# Case 1: gypsum / anhydrite with FeSO4 + CaCl2 + NaCl, pH 6 (pitzer.dat)
# ----------------------------------------------------------------------------
def case1():
    e = E["pitzer"]
    out = []
    print("\n=== CASE 1  Gypsum/Anhydrite SI, FeSO4 + CaCl2 + NaCl, pH 6  [pitzer.dat]")
    print(" CaCl2  NaCl |  FeSO4 1 mM   |  FeSO4 10 mM  |  FeSO4 100 mM | FeSO4 at SI_gyp=0 / SI_anh=0 (mmol/kg)")
    print("   m      m  |  gyp    anh   |  gyp    anh   |  gyp    anh   |")
    for c in (0.5, 0.05):
        for n in (0.5, 2.0, 5.0):
            cells = []
            for f in (0.001, 0.01, 0.1):
                comp = {"Na": n, "Ca": c, "Cl": n + 2 * c, "Fe": f, "S(6)": f}
                row, reag, added, ph0 = e.at_ph(comp, 6.0, si=("Gypsum", "Anhydrite"))
                track(added, f"case1 {reag}")
                g, a = si_val(row, "Gypsum"), si_val(row, "Anhydrite")
                cells.append((g, a))
                out.append(dict(CaCl2=c, NaCl=n, FeSO4=f, SI_gypsum=g, SI_anhydrite=a, I=row["mu"],
                                reagent=reag, reagent_mol=added))

            def si_of(logf, phase):
                f = 10 ** logf
                comp = {"Na": n, "Ca": c, "Cl": n + 2 * c, "Fe": f, "S(6)": f}
                row, *_ = e.at_ph(comp, 6.0, si=(phase,))
                return si_val(row, phase)
            fg = bisect(lambda x: si_of(x, "Gypsum"), -6, 0.3, tol=1e-3)
            fa = bisect(lambda x: si_of(x, "Anhydrite"), -6, 0.3, tol=1e-3)
            thr_g = None if fg is None else 1000 * 10 ** fg
            thr_a = None if fa is None else 1000 * 10 ** fa
            out.append(dict(CaCl2=c, NaCl=n, FeSO4_at_gyp_sat_mmol=thr_g, FeSO4_at_anh_sat_mmol=thr_a))
            s = " | ".join(f"{f2(g)}  {f2(a)}" for g, a in cells)
            print(f" {c:5.2f} {n:5.1f} | {s} | {thr_g:7.1f} / {thr_a:7.1f}")
    RES["case1"] = out


# ----------------------------------------------------------------------------
# Case 2: halite (pitzer.dat)
# ----------------------------------------------------------------------------
def case2():
    e = E["pitzer"]
    out = {}
    print("\n=== CASE 2  Halite SI, NaCl 5 m + CaCl2  [pitzer.dat]")
    for c in (0.0, 0.25, 0.5):
        row = e.initial({"Na": 5.0, "Ca": c, "Cl": 5.0 + 2 * c}, si=("Halite",))
        out[f"SI_halite_NaCl5_CaCl2_{c}"] = si_val(row, "Halite")
        print(f"  NaCl 5.00 + CaCl2 {c:4.2f}: SI_halite = {si_val(row, 'Halite'):6.3f}  (I = {row['mu']:.2f})")
    for c in (0.0, 0.25, 0.5):
        def f(n):
            row = e.initial({"Na": n, "Ca": c, "Cl": n + 2 * c}, si=("Halite",))
            return si_val(row, "Halite")
        nsat = bisect(f, 2.0, 7.5, tol=1e-5)
        # independent check: equilibrate CaCl2 solution with halite
        row = e.saturate({"Ca": c, "Cl": 2 * c} if c > 0 else {}, "Halite", totals=("Na",))
        nsat2 = row["Na(mol/kgw)"]
        out[f"NaCl_sat_CaCl2_{c}"] = nsat
        print(f"  halite saturation with CaCl2 {c:4.2f}: NaCl = {nsat:.3f} m (root find); "
              f"{nsat2:.3f} m (EQUILIBRIUM_PHASES)")
    # evaporation margin: concentrate NaCl 5 + CaCl2 c by factor k until halite saturates
    for c in (0.0, 0.25, 0.5):
        def h(k):
            row = e.initial({"Na": 5.0 * k, "Ca": c * k, "Cl": (5.0 + 2 * c) * k}, si=("Halite",))
            return si_val(row, "Halite")
        k = bisect(h, 1.0, 1.5, tol=1e-6)
        out[f"evap_factor_CaCl2_{c}"] = k
        print(f"  NaCl 5 + CaCl2 {c:4.2f}: halite saturates after losing {100 * (1 - 1 / k):.1f} % of the water"
              f" (concentration factor {k:.3f})")
    RES["case2"] = out


# ----------------------------------------------------------------------------
# Case 3: cotunnite (llnl.dat; minteq/wateq4f cross-checks)
# ----------------------------------------------------------------------------
def case3():
    out = {"SI": [], "solubility": []}
    print("\n=== CASE 3  Cotunnite SI, Pb(NO3)2 in NaCl, pH 5  [llnl.dat; (minteq.v4 / wateq4f)]")
    print("  NaCl |  Pb 0.01 mM          |  Pb 1 mM             |  Pb 10 mM            |  Pb 100 mM")
    for n in (0.5, 1.0, 2.0, 5.0):
        cells = []
        for p in (1e-5, 1e-3, 1e-2, 1e-1):
            vals = {}
            for key in ("llnl", "minteq", "wateq4f"):
                e = E[key]
                nm = e.n
                comp = {"Na": n, "Cl": n, nm["Pb"]: p, nm["N5"]: 2 * p}
                row, reag, added, ph0 = e.at_ph(comp, 5.0, si=("Cotunnite",))
                track(added, f"case3 {key} {reag}")
                vals[key] = si_val(row, "Cotunnite")
            out["SI"].append(dict(NaCl=n, Pb=p, **{f"SI_{k}": v for k, v in vals.items()}))
            cells.append(f"{f2(vals['llnl'])} ({f2(vals['minteq'])}/{f2(vals['wateq4f'])})")
        print(f"  {n:4.1f} | " + " | ".join(cells))

    print("\n  PbCl2 solubility = total dissolved Pb at cotunnite saturation (pH floats; mmol/kgw)")
    print("  medium        llnl     minteq.v4  wateq4f   [llnl: g PbCl2/kg water; pH]")
    for n in (0.0, 0.5, 1.0, 2.0, 5.0):
        vals = {}
        for key in ("llnl", "minteq", "wateq4f"):
            e = E[key]
            comp = {"Na": n, "Cl": n} if n > 0 else {}
            row = e.saturate(comp, "Cotunnite", totals=("Pb",))
            vals[key] = (1000 * row["Pb(mol/kgw)"], row["pH"])
        out["solubility"].append(dict(NaCl=n, **{f"Pb_mmolkg_{k}": v[0] for k, v in vals.items()}))
        lab = "pure water " if n == 0 else f"NaCl {n:3.1f} m "
        gl = vals["llnl"][0] * 278.1 / 1000
        print(f"  {lab}  {vals['llnl'][0]:7.2f}  {vals['minteq'][0]:7.2f}   {vals['wateq4f'][0]:7.2f}"
              f"     [{gl:5.2f} g/kg; pH {vals['llnl'][1]:.2f}]")

    # Pb speciation at 10 mM Pb, pH 5 (llnl) to show chloro complexation
    e = E["llnl"]
    print("\n  llnl Pb speciation (fraction of total Pb), Pb 10 mM, pH 5:")
    sp = ["Pb+2", "PbCl+", "PbCl2", "PbCl3-", "PbCl4-2", "PbNO3+"]
    for n in (0.5, 1.0, 2.0, 5.0):
        comp = {"Na": n, "Cl": n, "Pb(+2)": 0.01, "N(+5)": 0.02}
        row, *_ = e.at_ph(comp, 5.0, totals=("Pb",), mol=sp, act=("Pb+2",))
        tot = row["Pb(mol/kgw)"]
        fr = {s: mol(row, s) / tot for s in sp}
        lg = la(row, "Pb+2") - math.log10(mol(row, "Pb+2"))
        print(f"   NaCl {n:3.1f}: " + "  ".join(f"{s} {fr[s]:.3f}" for s in sp) + f"   log g(Pb2+) {lg:.2f}")
    RES["case3"] = out


# ----------------------------------------------------------------------------
# Case 4: carbonate buffer interference, 10 mM NaHCO3, 0.5 m NaCl, closed system
# ----------------------------------------------------------------------------
def case4():
    out = []
    print("\n=== CASE 4  10 mM NaHCO3 in 0.5 m NaCl, closed, pH fixed with HCl/NaOH")
    print("  Pb [llnl.dat]: SI cerussite / hydrocerussite   (minteq.v4 in parentheses)")
    for pH in (7.0, 8.0):
        for p in (1e-3, 1e-2):
            v = {}
            for key in ("llnl", "minteq"):
                e = E[key]
                nm = e.n
                comp = {"Na": 0.5 + 0.01, "Cl": 0.5, nm["C4"]: 0.01, nm["Pb"]: p, nm["N5"]: 2 * p}
                row, reag, added, ph0 = e.at_ph(comp, pH, si=("Cerussite", "Hydrocerussite"))
                track(added, f"case4 Pb {key} {reag}")
                v[key] = (si_val(row, "Cerussite"), si_val(row, "Hydrocerussite"), reag, added)
            out.append(dict(metal="Pb", pH=pH, M=p, llnl=v["llnl"], minteq=v["minteq"]))
            print(f"   pH {pH:.0f}  Pb {p*1e3:4.0f} mM: cerussite {f2(v['llnl'][0])} ({f2(v['minteq'][0])})  "
                  f"hydrocerussite {f2(v['llnl'][1])} ({f2(v['minteq'][1])})   "
                  f"[{v['llnl'][2]} {v['llnl'][3]*1e3:.2f} mmol]")
    print("  Fe(II) as FeCl2 [phreeqc.dat]: SI siderite   (llnl.dat / minteq.v4 in parentheses)")
    for pH in (7.0, 8.0):
        for fe in (1e-3, 1e-2):
            v = {}
            for key in ("phreeqc", "llnl", "minteq"):
                e = E[key]
                nm = e.n
                comp = {"Na": 0.5 + 0.01, "Cl": 0.5 + 2 * fe, nm["C4"]: 0.01, nm["Fe2"]: fe}
                row, reag, added, ph0 = e.at_ph(comp, pH, si=("Siderite",))
                track(added, f"case4 Fe {key} {reag}")
                v[key] = (si_val(row, "Siderite"), reag, added)
            out.append(dict(metal="Fe", pH=pH, M=fe, **{k: v[k] for k in v}))
            print(f"   pH {pH:.0f}  Fe {fe*1e3:4.0f} mM: siderite {f2(v['phreeqc'][0])} "
                  f"({f2(v['llnl'][0])} / {f2(v['minteq'][0])})   [{v['phreeqc'][1]} {v['phreeqc'][2]*1e3:.2f} mmol]")
    RES["case4"] = out


# ----------------------------------------------------------------------------
# Case 5: hydroxides at pH 9, 0.5 m NaCl (no carbonate)
# ----------------------------------------------------------------------------
def case5():
    out = []
    print("\n=== CASE 5  pH 9, 0.5 m NaCl, CO2-free")
    for p in (1e-3, 1e-2):
        e = E["llnl"]
        comp = {"Na": 0.5, "Cl": 0.5, "Pb(+2)": p, "N(+5)": 2 * p}
        r1, reag, added, _ = e.at_ph(comp, 9.0, si=("Litharge", "Massicot", "Paralaurionite", "Cotunnite"))
        track(added, "case5 Pb llnl")
        e2 = E["minteq"]
        comp2 = {"Na": 0.5, "Cl": 0.5, "Pb": p, "N(5)": 2 * p}
        r2, reag2, added2, _ = e2.at_ph(comp2, 9.0, si=("Pb(OH)2", "Litharge", "Massicot", "Laurionite", "Pb2(OH)3Cl"))
        d = dict(Pb=p, llnl={k: si_val(r1, k) for k in ("Litharge", "Massicot", "Paralaurionite")},
                 minteq={k: si_val(r2, k) for k in ("Pb(OH)2", "Litharge", "Massicot", "Laurionite", "Pb2(OH)3Cl")},
                 NaOH_mmol=added * 1e3)
        out.append(d)
        print(f"  Pb {p*1e3:4.0f} mM  llnl: litharge {f2(d['llnl']['Litharge'])} massicot {f2(d['llnl']['Massicot'])} "
              f"paralaurionite {f2(d['llnl']['Paralaurionite'])} | minteq.v4: Pb(OH)2 {f2(d['minteq']['Pb(OH)2'])} "
              f"litharge {f2(d['minteq']['Litharge'])} laurionite {f2(d['minteq']['Laurionite'])} "
              f"Pb2(OH)3Cl {f2(d['minteq']['Pb2(OH)3Cl'])}  [{reag} {added*1e3:.2f} mmol]")
    for fe in (1e-3, 1e-2):
        v = {}
        for key in ("llnl", "minteq"):
            e = E[key]
            comp = {"Na": 0.5, "Cl": 0.5 + 2 * fe, e.n["Fe2"]: fe}
            row, reag, added, _ = e.at_ph(comp, 9.0, si=("Fe(OH)2",))
            track(added, f"case5 Fe {key}")
            v[key] = (si_val(row, "Fe(OH)2"), added)
        out.append(dict(Fe=fe, SI_FeOH2_llnl=v["llnl"][0], SI_FeOH2_minteq=v["minteq"][0]))
        print(f"  Fe {fe*1e3:4.0f} mM  Fe(OH)2: llnl {f2(v['llnl'][0])}  minteq.v4 {f2(v['minteq'][0])}"
              f"   [NaOH {v['llnl'][1]*1e3:.2f} mmol]")
    RES["case5"] = out


# ----------------------------------------------------------------------------
# Case 6: H2S(aq) fraction of total sulfide, 1 mM, 0.5 m NaCl
# ----------------------------------------------------------------------------
def case6():
    out = []
    print("\n=== CASE 6  H2S(aq) fraction of total S(-2) (1 mM, 0.5 m NaCl)")
    print("  pH   llnl   phreeqc  minteq.v4  wateq4f")
    for pH in (4.0, 6.0, 7.0, 8.0, 9.0):
        v = {}
        for key in ("llnl", "phreeqc", "minteq", "wateq4f"):
            e = E[key]
            comp = {"Na": 0.5, "Cl": 0.5, "S(-2)": 0.001}
            row, reag, added, _ = e.at_ph(comp, pH, totals=("S(-2)",), mol=("H2S", "HS-"))
            track(added, f"case6 {key}")
            v[key] = mol(row, "H2S") / row["S(-2)(mol/kgw)"]
        out.append(dict(pH=pH, **v))
        print(f"  {pH:3.0f}  " + "  ".join(f"{v[k]:6.3f}" for k in ("llnl", "phreeqc", "minteq", "wateq4f")))
    # apparent pK1 (pH at 50 % H2S) per database
    for key in ("llnl", "phreeqc", "minteq", "wateq4f"):
        e = E[key]

        def g(pH):
            row, *_ = e.at_ph({"Na": 0.5, "Cl": 0.5, "S(-2)": 0.001}, pH, totals=("S(-2)",), mol=("H2S",))
            return mol(row, "H2S") / row["S(-2)(mol/kgw)"] - 0.5
        pk = bisect(g, 5.5, 8.0, tol=1e-4)
        print(f"  apparent pK1 (50 % H2S) {key}: {pk:.2f}")
        out.append(dict(db=key, apparent_pK1=pk))
    RES["case6"] = out


# ----------------------------------------------------------------------------
# Case 7: galena (llnl) and mackinawite / FeS(ppt) (phreeqc.dat) on a grid
# ----------------------------------------------------------------------------
PB_SP = ["Pb+2", "PbCl+", "PbCl2", "PbCl3-", "PbCl4-2", "PbOH+", "Pb(OH)2"]


def galena(key, n, m, pH, grid=True):
    e = E[key]
    nm = e.n
    comp = {"Na": n, "Cl": n + 2 * m, nm["Pb"]: m, "S(-2)": m}
    species = PB_SP + (["Pb(HS)2", "Pb(HS)3-"] if key == "minteq" else [])
    row, reag, added, _ = e.at_ph(comp, pH, si=("Galena",), totals=("Pb",), mol=species, act=("Pb+2",))
    if grid:
        track(added, f"case7 Pb {key} {reag} NaCl {n} pH {pH} M {m}")
    return row, reag, added


def fes(key, n, m, pH, grid=True):
    e = E[key]
    comp = {"Na": n, "Cl": n + 2 * m, e.n["Fe2"]: m, "S(-2)": m}
    row, reag, added, _ = e.at_ph(comp, pH, si=("Mackinawite", "FeS(ppt)"), totals=("Fe",), mol=("Fe+2",))
    if grid:
        track(added, f"case7 Fe {key} {reag} NaCl {n} pH {pH} M {m}")
    return row, reag, added


def case7():
    out = []
    print("\n=== CASE 7  metal = sulfide; SI galena [llnl] (minteq.v4) ; SI mackinawite / FeS(ppt) [phreeqc.dat] (minteq.v4 mack)")
    print(" NaCl  pH  M=S mM | galena llnl (minteq) | mack  FeS(ppt) (minteq mack) | free Pb2+ frac llnl, log g")
    for n in (0.5, 5.0):
        for pH in (4.0, 6.0, 9.0):
            for m in (1e-5, 1e-4, 1e-2):
                rg, reag_g, add_g = galena("llnl", n, m, pH)
                rg2, *_ = galena("minteq", n, m, pH)
                rf, reag_f, add_f = fes("phreeqc", n, m, pH)
                rf2, *_ = fes("minteq", n, m, pH)
                free = mol(rg, "Pb+2") / rg["Pb(mol/kgw)"]
                lg = la(rg, "Pb+2") - math.log10(mol(rg, "Pb+2"))
                d = dict(NaCl=n, pH=pH, M=m, SI_galena_llnl=si_val(rg, "Galena"),
                         SI_galena_minteq=si_val(rg2, "Galena"),
                         SI_mack_phreeqc=si_val(rf, "Mackinawite"), SI_FeSppt_phreeqc=si_val(rf, "FeS(ppt)"),
                         SI_mack_minteq=si_val(rf2, "Mackinawite"),
                         free_Pb_frac_llnl=free, logg_Pb_llnl=lg,
                         Pb_species_frac_llnl={s: mol(rg, s) / rg["Pb(mol/kgw)"] for s in PB_SP},
                         free_Pb_frac_minteq=mol(rg2, "Pb+2") / rg2["Pb(mol/kgw)"],
                         reagent_Pb=(reag_g, add_g), reagent_Fe=(reag_f, add_f))
                out.append(d)
                print(f" {n:4.1f} {pH:3.0f} {m*1e3:6.2f} |   {f2(d['SI_galena_llnl'])} ({f2(d['SI_galena_minteq'])})     |"
                      f" {f2(d['SI_mack_phreeqc'])} {f2(d['SI_FeSppt_phreeqc'])}    ({f2(d['SI_mack_minteq'])})      |"
                      f"  {free:.4f}  {lg:5.2f}")
    # Pb speciation summary at the two NaCl levels (1e-4 m, pH 6)
    print("\n  llnl Pb speciation, Pb = S = 0.1 mM, pH 6:")
    for d in out:
        if d["M"] == 1e-4 and d["pH"] == 6.0:
            print(f"   NaCl {d['NaCl']}: " + "  ".join(f"{s} {v:.3f}" for s, v in d["Pb_species_frac_llnl"].items()))

    # equimolar concentration at which SI = 0
    print("\n  Equimolar metal = sulfide concentration (mmol/kg) giving SI = 0")
    print("  NaCl pH | galena llnl | galena minteq | mackinawite phreeqc | FeS(ppt) phreeqc")
    thr = []
    for n in (0.5, 5.0):
        for pH in (4.0, 6.0, 9.0):
            res = {}
            for lab, fn, key, ph in (("gal_llnl", galena, "llnl", "Galena"), ("gal_minteq", galena, "minteq", "Galena"),
                                     ("mack", fes, "phreeqc", "Mackinawite"), ("fesppt", fes, "phreeqc", "FeS(ppt)")):
                def s(logm):
                    row, *_ = fn(key, n, 10 ** logm, pH, grid=False)
                    return si_val(row, ph)
                lo, hi = -10.0, -0.7
                slo, shi = s(lo), s(hi)
                if slo > 0:
                    res[lab] = "<1e-7"          # supersaturated even at 1e-10 m
                elif shi < 0:
                    res[lab] = ">200"           # undersaturated even at 0.2 m
                else:
                    r = bisect(s, lo, hi, tol=1e-3)
                    res[lab] = 1000 * 10 ** r
            thr.append(dict(NaCl=n, pH=pH, **res))

            def fm(x):
                return f"{x:>10s}" if isinstance(x, str) else f"{x:10.2e}"
            print(f"  {n:3.1f} {pH:3.0f} | {fm(res['gal_llnl'])} | {fm(res['gal_minteq'])}  | {fm(res['mack'])}"
                  f"          | {fm(res['fesppt'])}")
    RES["case7"] = {"grid": out, "SI0_equimolar_mmolkg": thr}


if __name__ == "__main__":
    case1()
    case2()
    case3()
    case4()
    case5()
    case6()
    case7()
    print(f"\nLargest pH-adjustment reagent dose: {MAX_REAGENT['mol']*1e3:.2f} mmol/kgw ({MAX_REAGENT['where']})")
    with open(HERE / "results.json", "w") as fh:
        json.dump(RES, fh, indent=1, default=str)
    print("results.json written")
