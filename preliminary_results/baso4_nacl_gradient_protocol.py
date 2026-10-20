"""
OT-2 Protocol: BaSO₄ Precipitation Matrix with NaCl Gradient

🥇 Top recommended preliminary experiment for ACS PRF DNI proposal.

Closes the computational–experimental loop by overlaying experimental
precipitation boundaries on Pitzer SI predictions from
precipitation_boundary_map.py.

Reaction:
    BaCl₂(aq) + Na₂SO₄(aq) → BaSO₄(s)↓ (white) + 2 NaCl(aq)

Plate layout (96-well, flat-bottom, clear):
    - Rows A–H: 8 Ba²⁺ concentrations (0.1–10 mM, diluted from 0.1 M stock)
    - Columns 1–12: 12 NaCl concentrations (0–2 M)
    - [SO₄²⁻] held constant at 0.01 M in every well (added last to trigger)
    - Total volume per well: 200 µL

Reagent setup (reservoir slots):
    Slot 1 (reservoir):  Column 1 = 0.1 M BaCl₂ stock
                         Column 2 = 5 M NaCl stock
                         Column 3 = DI water
                         Column 4 = 0.1 M Na₂SO₄ (trigger reagent, added last)

Safety:
    - Ba²⁺ is toxic by ingestion; dilute solutions with standard PPE are safe.
    - Standard waste disposal for barium-containing solutions.

Requirements:
    Opentrons OT-2 with GEN2 single-channel P300 pipette (left mount)
    Opentrons 96-well flat-bottom plate
    NEST 12-column reservoir (or similar)
    200 µL filter tips

Usage:
    Upload to Opentrons App or run via:
        opentrons_simulate baso4_nacl_gradient_protocol.py

References:
    - Protocol aligns with PRELIMINARY_RESULTS_PLAN.md experiment #5
    - Pitzer predictions from precipitation_boundary_map.py
"""

from opentrons import protocol_api

metadata = {
    "protocolName": "BaSO4 NaCl Gradient Precipitation",
    "author": "Copilot <copilot@github.com>",
    "description": "BaSO4 precipitation matrix: 8 [Ba2+] x 12 [NaCl] at fixed [SO42-]",
    "apiLevel": "2.15",
}

# ---------------------------------------------------------------------------
# Experimental parameters
# ---------------------------------------------------------------------------
TOTAL_WELL_VOLUME = 200  # µL per well

# Ba²⁺ concentrations in the well (mM) — 8 levels for rows A-H
BA_CONC_MM = [0.1, 0.25, 0.5, 1.0, 2.0, 4.0, 7.0, 10.0]

# NaCl concentrations in the well (M) — 12 levels for columns 1-12
NACL_CONC_M = [0.0, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

# Fixed SO₄²⁻ concentration in the well (M)
SO4_CONC_M = 0.01

# Stock concentrations
BA_STOCK_M = 0.1       # 0.1 M BaCl₂
NACL_STOCK_M = 5.0     # 5 M NaCl
SO4_STOCK_M = 0.1      # 0.1 M Na₂SO₄

# Reservoir column assignments (0-indexed)
RES_BA = 0        # Column 1: BaCl₂ stock
RES_NACL = 1      # Column 2: NaCl stock
RES_WATER = 2     # Column 3: DI water
RES_SO4 = 3       # Column 4: Na₂SO₄ (trigger, added last)


def compute_volumes(ba_mm, nacl_m, so4_m, total_vol):
    """Compute pipetting volumes for one well.

    Returns dict with volumes (µL) of Ba stock, NaCl stock, SO4 stock, and water.
    """
    ba_m = ba_mm / 1000.0  # convert mM to M

    vol_ba = (ba_m / BA_STOCK_M) * total_vol       # Ba stock volume
    vol_nacl = (nacl_m / NACL_STOCK_M) * total_vol  # NaCl stock volume
    vol_so4 = (so4_m / SO4_STOCK_M) * total_vol     # SO4 stock volume
    vol_water = total_vol - vol_ba - vol_nacl - vol_so4

    if vol_water < 0:
        raise ValueError(
            f"Negative water volume for Ba={ba_mm} mM, NaCl={nacl_m} M: "
            f"sum={vol_ba + vol_nacl + vol_so4:.1f} µL > {total_vol} µL"
        )

    return {
        "ba": round(vol_ba, 1),
        "nacl": round(vol_nacl, 1),
        "so4": round(vol_so4, 1),
        "water": round(vol_water, 1),
    }


def run(protocol: protocol_api.ProtocolContext):
    """Execute the BaSO₄ + NaCl gradient protocol."""

    # --- Load labware ---
    tips = protocol.load_labware("opentrons_96_filtertiprack_200ul", 4)
    plate = protocol.load_labware("corning_96_wellplate_360ul_flat", 2)
    reservoir = protocol.load_labware("nest_12_reservoir_15ml", 1)

    # --- Load pipette ---
    pipette = protocol.load_instrument(
        "p300_single_gen2", "left", tip_racks=[tips]
    )

    # --- Pre-compute all volumes ---
    well_volumes = {}
    for row_idx, ba_mm in enumerate(BA_CONC_MM):
        for col_idx, nacl_m in enumerate(NACL_CONC_M):
            vols = compute_volumes(ba_mm, nacl_m, SO4_CONC_M, TOTAL_WELL_VOLUME)
            well_name = f"{chr(65 + row_idx)}{col_idx + 1}"
            well_volumes[well_name] = vols

    protocol.comment("=" * 50)
    protocol.comment("BaSO₄ + NaCl Gradient Precipitation Protocol")
    protocol.comment(f"Plate: {len(BA_CONC_MM)} [Ba²⁺] × {len(NACL_CONC_M)} [NaCl]")
    protocol.comment(f"[SO₄²⁻] = {SO4_CONC_M*1000:.0f} mM (fixed)")
    protocol.comment("=" * 50)

    # --- Step 1: Dispense DI water ---
    protocol.comment("Step 1: Dispensing DI water to all wells")
    for well_name, vols in well_volumes.items():
        if vols["water"] >= 5:  # skip very small volumes
            pipette.pick_up_tip()
            pipette.aspirate(vols["water"], reservoir.columns()[RES_WATER][0])
            pipette.dispense(vols["water"], plate.wells_by_name()[well_name])
            pipette.drop_tip()

    # --- Step 2: Dispense NaCl stock ---
    protocol.comment("Step 2: Dispensing NaCl stock")
    for well_name, vols in well_volumes.items():
        if vols["nacl"] >= 5:
            pipette.pick_up_tip()
            pipette.aspirate(vols["nacl"], reservoir.columns()[RES_NACL][0])
            pipette.dispense(vols["nacl"], plate.wells_by_name()[well_name])
            pipette.drop_tip()

    # --- Step 3: Dispense BaCl₂ stock ---
    protocol.comment("Step 3: Dispensing BaCl₂ stock")
    for well_name, vols in well_volumes.items():
        if vols["ba"] >= 1:
            pipette.pick_up_tip()
            pipette.aspirate(vols["ba"], reservoir.columns()[RES_BA][0])
            pipette.dispense(vols["ba"], plate.wells_by_name()[well_name])
            pipette.mix(3, min(vols["ba"] + vols["nacl"] + vols["water"], 100))
            pipette.drop_tip()

    # --- Step 4: Trigger — add Na₂SO₄ last ---
    protocol.comment("Step 4: Adding Na₂SO₄ trigger reagent (LAST)")
    protocol.comment(">>> Image plate BEFORE and AFTER this step <<<")
    for well_name, vols in well_volumes.items():
        if vols["so4"] >= 1:
            pipette.pick_up_tip()
            pipette.aspirate(vols["so4"], reservoir.columns()[RES_SO4][0])
            pipette.dispense(vols["so4"], plate.wells_by_name()[well_name])
            pipette.mix(3, min(TOTAL_WELL_VOLUME * 0.5, 150))
            pipette.drop_tip()

    protocol.comment("=" * 50)
    protocol.comment("Protocol complete!")
    protocol.comment("Image plate at: 0 min, 2 min, 10 min, 30 min")
    protocol.comment("Score each well: clear (0) / faint turbidity (1) / precipitate (2)")
    protocol.comment("=" * 50)
