"""Thin PHREEQC helper on top of phreeqpython's bundled IPhreeqc (VIPhreeqc 3.7.3).

- Loads a database (bundled pitzer.dat / phreeqc.dat, or USGS llnl.dat,
  minteq.v4.dat, wateq4f.dat downloaded into db/ next to this file from
  https://github.com/usgs-coupled/phreeqc3/tree/master/database).
- Defines a Fix_H+ pseudo-phase (H+ = H+, log_k 0) so that
  EQUILIBRIUM_PHASES "Fix_H+ -pH <reagent> 10" doses NaOH or HCl to a target pH.
- Runs raw PHREEQC input and returns SELECTED_OUTPUT rows as dicts.
"""
from pathlib import Path

import phreeqpython
from phreeqpython.viphreeqc import VIPhreeqc

BUNDLED = Path(phreeqpython.__file__).parent / "database"
DL = Path(__file__).resolve().parent / "db"
DB_PATHS = {
    "pitzer": BUNDLED / "pitzer.dat",     # bundled with phreeqpython 1.6.2
    "phreeqc": BUNDLED / "phreeqc.dat",   # bundled with phreeqpython 1.6.2
    "llnl": DL / "llnl.dat",              # usgs-coupled/phreeqc3 master
    "minteq": DL / "minteq.v4.dat",       # usgs-coupled/phreeqc3 master
    "wateq4f": DL / "wateq4f.dat",        # usgs-coupled/phreeqc3 master
}

# master-species spellings differ between databases
NAMES = {
    "llnl":    {"Fe2": "Fe(+2)", "Pb": "Pb(+2)", "S6": "S(+6)", "S-2": "S(-2)", "C4": "C(+4)", "N5": "N(+5)"},
    "phreeqc": {"Fe2": "Fe(2)",  "Pb": "Pb",     "S6": "S(6)",  "S-2": "S(-2)", "C4": "C(4)",  "N5": "N(5)"},
    "minteq":  {"Fe2": "Fe(2)",  "Pb": "Pb",     "S6": "S(6)",  "S-2": "S(-2)", "C4": "C(4)",  "N5": "N(5)"},
    "wateq4f": {"Fe2": "Fe(2)",  "Pb": "Pb",     "S6": "S(6)",  "S-2": "S(-2)", "C4": "C(4)",  "N5": "N(5)"},
    "pitzer":  {"Fe2": "Fe",     "S6": "S(6)",   "C4": "C(4)"},
}

MISSING = -999.0  # PHREEQC prints -999.999 for SI of phases that cannot be computed


class Engine:
    def __init__(self, key):
        self.key = key
        self.ip = VIPhreeqc()
        self.ip.load_database(str(DB_PATHS[key]))
        if self.ip.phc_database_error_count:
            raise RuntimeError(f"{key}: database load errors: {self.ip.get_error_string()[:500]}")
        self.ip.run_string("PHASES\nFix_H+\n    H+ = H+\n    log_k 0.0\nEND\n")
        self.n = NAMES[key]

    def run(self, text):
        self.ip.run_string(text)
        arr = self.ip.get_selected_output_array()
        hdr = arr[0]
        return [dict(zip(hdr, r)) for r in arr[1:]]

    # ------------------------------------------------------------------
    @staticmethod
    def solution_block(comp, ph_line="pH 7 charge", pe=4.0):
        lines = ["SOLUTION 1", "    temp 25", "    units mol/kgw", f"    {ph_line}", f"    pe {pe:.4f}"]
        for k, v in comp.items():
            if v and v > 0:
                lines.append(f"    {k:<8} {v:.12g}")
        return "\n".join(lines) + "\n"

    @staticmethod
    def sel_block(si=(), totals=(), mol=(), act=(), eq=()):
        s = ["SELECTED_OUTPUT 1", "    -reset false", "    -state true", "    -pH true",
             "    -ionic_strength true", "    -water true", "    -charge_balance true"]
        if si:
            s.append("    -si " + " ".join(si))
        if totals:
            s.append("    -totals " + " ".join(totals))
        if mol:
            s.append("    -molalities " + " ".join(mol))
        if act:
            s.append("    -activities " + " ".join(act))
        if eq:
            s.append("    -equilibrium_phases " + " ".join(eq))
        return "\n".join(s) + "\n"

    def initial(self, comp, ph_line="pH 7 charge", pe=4.0, **sel):
        rows = self.run(self.solution_block(comp, ph_line, pe) + self.sel_block(**sel) + "END\n")
        return rows[-1]

    def reducing_pe(self, comp, pe_plus_ph=2.5):
        """Initial pe for sulfidic solutions: pe + pH = 2.5 (log aO2 ~ -76, log aH2 ~ -8),
        so species written with O2/e- (e.g. llnl polysulfides) do not form artificially."""
        pe = 0.0
        for _ in range(4):
            ph0 = self.initial(comp, pe=pe)["pH"]
            pe = pe_plus_ph - ph0
        return pe

    def at_ph(self, comp, pH, reagent=None, reducing=None, **sel):
        """Charge-balanced initial solution, then dose NaOH (pH up) or HCl (pH down)
        through the Fix_H+ pseudo-phase until pH = target. Returns (row, reagent, mol_added, pH0).
        Sulfide-bearing solutions get a reducing initial pe (see reducing_pe)."""
        if reducing is None:
            reducing = any(k.startswith("S(-2)") for k in comp)
        pe = self.reducing_pe(comp) if reducing else 4.0
        r0 = self.initial(comp, pe=pe)
        ph0 = r0["pH"]
        if reagent is None:
            reagent = "NaOH" if ph0 < pH else "HCl"
        eq = tuple(sel.pop("eq", ())) + ("Fix_H+",)
        text = (self.solution_block(comp, pe=pe) +
                f"EQUILIBRIUM_PHASES 1\n    Fix_H+ {-pH:.4f} {reagent} 10\n" +
                self.sel_block(eq=eq, **sel) + "END\n")
        row = self.run(text)[-1]
        added = -row["d_Fix_H+"]  # dissolved (added to solution) = negative delta
        if abs(row["pH"] - pH) > 1e-3:
            raise RuntimeError(f"pH not reached: {row['pH']} vs {pH}")
        return row, reagent, added, ph0

    def saturate(self, comp, phase, **sel):
        """Equilibrate initial solution with a mineral (no pH control). Returns reaction row."""
        eq = tuple(sel.pop("eq", ())) + (phase,)
        text = (self.solution_block(comp) + f"EQUILIBRIUM_PHASES 1\n    {phase} 0.0 10\n" +
                self.sel_block(eq=eq, **sel) + "END\n")
        return self.run(text)[-1]


def si_val(row, phase):
    v = row.get(f"si_{phase}")
    if v is None or v <= MISSING:
        return None
    return v


def bisect(f, lo, hi, tol=1e-4, maxit=80):
    """Root of monotonic f on [lo, hi]."""
    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        return None
    for _ in range(maxit):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if abs(hi - lo) < tol:
            break
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def mol(row, sp):
    """Molality of a species from a SELECTED_OUTPUT row (column 'm_<sp>(mol/kgw)')."""
    v = row.get(f"m_{sp}(mol/kgw)", row.get(f"m_{sp}"))
    if v is None:
        raise KeyError(sp)
    return v


def la(row, sp):
    """log10 activity of a species (column 'la_<sp>')."""
    v = row.get(f"la_{sp}")
    if v is None:
        raise KeyError(sp)
    return v
