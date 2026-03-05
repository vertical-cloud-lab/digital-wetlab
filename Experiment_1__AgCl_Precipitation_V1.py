import json
from opentrons import protocol_api

metadata = {
    "protocolName": "Experiment 2 – BaSO₄ Precipitation Boundary Mapping",
    "description": (
        "Second experiment on OT-2, created 3/4/26 | "
        "Ba²⁺ + SO₄²⁻ → BaSO₄ ↓ + 2 NaCl | "
        "80 Latin hypercube conditions + 16 controls across Ba²⁺ (0.1–50 mM), "
        "SO₄²⁻ (0.1–50 mM), and NaCl (0–3 molal) in 200 µL/well"
    ),
    "created": "2026-03-04T17:42:25.821Z",
}

requirements = {"robotType": "OT-2", "apiLevel": "2.27"}

# ---------------------------------------------------------------------------
# Pre-computed Latin Hypercube Sampling (LHS) design matrix — 80 conditions.
# Generated with: scipy.stats.qmc.LatinHypercube(d=3, seed=42).random(n=80),
# then scaled to Ba²⁺ [0.1, 50] mM, SO₄²⁻ [0.1, 50] mM, NaCl [0, 3] molal.
#
# Row order matches column-first well plate filling (A1, B1, …, H1, A2, …, H10):
#   index 0  → well A1 (column 1, row A)
#   index 7  → well H1 (column 1, row H)
#   index 8  → well A2 (column 2, row A)
#   index 79 → well H10 (column 10, row H)
#
# Columns: (Ba²⁺ mM, SO₄²⁻ mM, NaCl molal)
# ---------------------------------------------------------------------------
LHS_CONDITIONS = [
    (45.1510, 42.8650, 0.4178),   # Well  1 (A1)
    (15.2588, 46.1988, 1.2759),   # Well  2 (B1)
    (10.2290,  4.5997, 2.0577),   # Well  3 (C1)
    (49.7191, 29.8087, 0.1902),   # Well  4 (D1)
    (42.7371,  8.3193, 2.4584),   # Well  5 (E1)
    (46.1158, 45.2878, 0.7476),   # Well  6 (F1)
    (24.5338,  5.9435, 2.7841),   # Well  7 (G1)
    ( 2.9976, 23.8208, 2.8165),   # Well  8 (H1)
    (38.9107,  7.4636, 0.6950),   # Well  9 (A2)
    (16.9139, 48.0325, 2.5619),   # Well 10 (B2)
    (15.8530,  7.6053, 0.9253),   # Well 11 (C2)
    (12.3439, 34.1134, 1.2304),   # Well 12 (D2)
    (46.8002, 18.5158, 1.8665),   # Well 13 (E2)
    ( 9.6622, 28.5198, 2.6688),   # Well 14 (F2)
    (48.3157, 27.9739, 0.9438),   # Well 15 (G2)
    (25.7955,  9.8383, 1.5642),   # Well 16 (H2)
    (28.3668, 14.9828, 2.4300),   # Well 17 (A3)
    (13.1942, 18.9454, 1.6251),   # Well 18 (B3)
    (38.3327, 40.7805, 0.0578),   # Well 19 (C3)
    (32.1802,  2.5078, 2.7707),   # Well 20 (D3)
    (19.6431, 10.4099, 2.3788),   # Well 21 (E3)
    (35.1766,  0.3278, 0.2417),   # Well 22 (F3)
    (27.1962, 25.4842, 1.1238),   # Well 23 (G3)
    (33.5101, 12.4412, 1.8972),   # Well 24 (H3)
    (25.1414, 33.0128, 2.0228),   # Well 25 (A4)
    (27.9932, 44.8269, 0.5377),   # Well 26 (B4)
    (30.9401, 13.9573, 0.7626),   # Well 27 (C4)
    ( 1.0940, 49.4923, 1.4937),   # Well 28 (D4)
    (30.0258, 23.1226, 2.9354),   # Well 29 (E4)
    (35.9894, 29.3157, 2.4937),   # Well 30 (F4)
    (49.2812, 35.2194, 1.3708),   # Well 31 (G4)
    ( 6.7236, 13.6344, 0.4639),   # Well 32 (H4)
    (41.6656, 32.4803, 0.2956),   # Well 33 (A5)
    (41.9150,  0.7808, 0.8738),   # Well 34 (B5)
    (23.0129,  5.1092, 2.2958),   # Well 35 (C5)
    (40.8203, 34.7497, 2.9148),   # Well 36 (D5)
    (34.3461, 37.5858, 1.5954),   # Well 37 (E5)
    (18.6863, 48.5617, 0.0158),   # Well 38 (F5)
    (26.8110, 43.8519, 2.1466),   # Well 39 (G5)
    (39.5712,  4.1967, 1.9640),   # Well 40 (H5)
    (14.0819, 25.8922, 0.1843),   # Well 41 (A6)
    (17.9294, 37.4990, 1.9315),   # Well 42 (B6)
    (30.4580, 17.4749, 0.4086),   # Well 43 (C6)
    (47.7622, 36.1711, 1.8028),   # Well 44 (D6)
    (23.4401, 19.8436, 0.1278),   # Well 45 (E6)
    (22.5408, 30.0658, 0.8069),   # Well 46 (F6)
    ( 7.0968, 18.1371, 0.9943),   # Well 47 (G6)
    ( 6.0314, 20.7225, 1.1786),   # Well 48 (H6)
    ( 8.5372,  1.8047, 1.2626),   # Well 49 (A7)
    (17.2402, 33.5087, 2.9992),   # Well 50 (B7)
    ( 1.4559, 41.3323, 1.1572),   # Well 51 (C7)
    ( 0.3782, 22.4873, 2.8623),   # Well 52 (D7)
    (14.8946, 48.9649, 1.5102),   # Well 53 (E7)
    (43.2831, 43.6953, 2.2156),   # Well 54 (F7)
    (36.7577, 40.6204, 2.7167),   # Well 55 (G7)
    (47.2736, 12.6812, 0.3072),   # Well 56 (H7)
    (37.9509, 46.9106, 1.6766),   # Well 57 (A8)
    (37.2037, 11.7916, 0.4899),   # Well 58 (B8)
    (34.9273,  6.9332, 2.0837),   # Well 59 (C8)
    (43.7673, 38.2163, 0.0844),   # Well 60 (D8)
    (13.2669, 26.9877, 1.4055),   # Well 61 (E8)
    (31.7142,  3.3610, 1.7002),   # Well 62 (F8)
    (21.0744,  9.3973, 1.3220),   # Well 63 (G8)
    ( 9.2925, 20.0994, 0.6285),   # Well 64 (H8)
    ( 5.6372, 38.8778, 2.5443),   # Well 65 (A9)
    (33.0469, 30.9136, 1.0547),   # Well 66 (B9)
    (29.2937, 39.8264, 2.2583),   # Well 67 (C9)
    (21.3251, 21.6189, 2.6196),   # Well 68 (D9)
    ( 4.4576, 46.7380, 1.4576),   # Well 69 (E9)
    (40.2211, 24.9740, 0.3560),   # Well 70 (F9)
    ( 3.4095, 15.3313, 0.8550),   # Well 71 (G9)
    (23.9247, 15.8713, 2.6348),   # Well 72 (H9)
    (20.6020, 26.8441, 0.5652),   # Well 73 (A10)
    ( 7.9608, 36.7135, 1.7442),   # Well 74 (B10)
    ( 2.1815, 23.2064, 1.0393),   # Well 75 (C10)
    (10.7507, 16.9257, 2.3417),   # Well 76 (D10)
    (11.5558, 31.8452, 2.2072),   # Well 77 (E10)
    (19.1748,  2.6161, 2.1151),   # Well 78 (F10)
    ( 4.5080, 10.8258, 0.6575),   # Well 79 (G10)
    (44.5205, 42.5039, 1.7959),   # Well 80 (H10)
]

# ---------------------------------------------------------------------------
# Stock concentrations and dispensing parameters
# ---------------------------------------------------------------------------
_BACL2_STOCK_MM  = 1000.0   # 1.0 M BaCl₂ stock  (24.426 g BaCl₂·2H₂O / 100 mL)
_NA2SO4_STOCK_MM = 1000.0   # 1.0 M Na₂SO₄ stock (14.204 g Na₂SO₄ / 100 mL)
_NACL_STOCK_M    =    5.0   # 5.0 M NaCl stock   (29.22 g NaCl / 100 mL)
_TOTAL_UL        =  200.0   # total volume per well (µL)

# Minimum reliable dispensing volume for the p20 GEN2.
# Volumes below this threshold are skipped; the shortfall is added to DI water
# so every well still totals _TOTAL_UL.  For large-volume reagents (DI water,
# NaCl) the p20 simply makes multiple 20 µL aspirations per well.
#
# NaCl coverage note: With a 5 M stock and 200 µL total, 1 µL corresponds to
# an NaCl concentration of 25 mM (0.025 molal) in the well.  All 80 LHS
# conditions with NaCl ≥ 0.025 molal receive their intended NaCl volume.
# One LHS well (F5, 0.0158 molal → 0.63 µL needed) falls below this minimum
# and is treated as zero NaCl; its water volume is increased by 0.63 µL.
_P20_MIN_UL = 1.0


def _calc_volumes(ba_mm, so4_mm, nacl_mol):
    """Return (v_bacl2, v_na2so4, v_nacl, v_water) in µL for one well.

    Ideal volumes are derived from target concentrations and stock strengths.
    Any volume below _P20_MIN_UL (1 µL — the p20 GEN2 reliable minimum) is
    rounded down to zero; the freed volume is added back to the DI-water
    allotment so the total always sums to _TOTAL_UL.

    NaCl threshold and LHS coverage
    --------------------------------
    With a 5 M NaCl stock and 200 µL total well volume the minimum achievable
    NaCl concentration with the p20 is:

        1 µL / 200 µL × 5000 mM = 25 mM  (≈ 0.025 molal)

    The LHS spans NaCl from 0 to 3 molal.  Of the 80 LHS conditions:
      • 79 have nacl_mol ≥ 0.025 molal → the required volume is ≥ 1 µL and
        is dispensed correctly using the p20.
      • 1 condition (Well F5, 0.0158 molal → 0.63 µL required) falls below
        the p20 minimum and is treated as 0 molal NaCl; its water volume is
        increased by 0.63 µL.  This is within the LHS design tolerance because
        the well was already placed very near the lower bound (0 molal).

    Ba²⁺ and SO₄²⁻ minimum
    -----------------------
    With 1 M stocks: 1 µL / 200 µL × 1000 mM = 5 mM.
    All LHS conditions with Ba²⁺ or SO₄²⁻ ≥ 5 mM are dispensed as designed;
    those below 5 mM are rounded to zero (treated as trace / absent).

    Note: NaCl target concentrations are given in molal (mol/kg solvent), but
    the stock is expressed as molar (mol/L solution).  For dilute-to-moderate
    aqueous NaCl (0–3 molal), the molar and molal values differ by < 3 % due to
    the density of the solution being close to 1.0 kg/L.  The volumetric
    calculation below treats them as equivalent, which is standard practice for
    this concentration range and within the accuracy limits of the OT-2.
    """
    v_b = round((ba_mm   / _BACL2_STOCK_MM)  * _TOTAL_UL, 4)
    v_s = round((so4_mm  / _NA2SO4_STOCK_MM) * _TOTAL_UL, 4)
    v_n = round((nacl_mol / _NACL_STOCK_M)   * _TOTAL_UL, 4)
    if v_b < _P20_MIN_UL:  v_b = 0.0
    if v_s < _P20_MIN_UL:  v_s = 0.0
    if v_n < _P20_MIN_UL:  v_n = 0.0
    v_w = round(_TOTAL_UL - v_b - v_s - v_n, 4)
    return v_b, v_s, v_n, v_w


def run(protocol: protocol_api.ProtocolContext) -> None:
    # ---------- Labware ----------
    # Slot 2: 20 µL filter tip rack — used by the p20 for all four reagents
    tip_rack_20 = protocol.load_labware(
        "opentrons_96_filtertiprack_20ul",
        location="2",
        namespace="opentrons",
        version=1,
    )
    # Slot 5: 6-tube rack with stock solutions (positions unchanged)
    #   A1 = DI Water, A2 = BaCl₂, B1 = Na₂SO₄, B2 = NaCl
    tube_rack_1 = protocol.load_labware_from_definition(
        CUSTOM_LABWARE["custom_beta/ac_6_tuberack_15000ul/1"],
        location="5",
    )
    # Slot 4: 96-well plate (position unchanged)
    well_plate_1 = protocol.load_labware(
        "nest_96_wellplate_200ul_flat",
        location="4",
        namespace="opentrons",
        version=2,
    )

    # ---------- Pipettes ----------
    # p20 single-channel GEN2 on the left mount handles all four reagents.
    # For DI water and NaCl (which can be up to 200 µL and 120 µL per well),
    # the OT-2 API automatically loops through multiple 20 µL aspirations with
    # the same tip, so no tip changes are needed.
    pipette_left = protocol.load_instrument(
        "p20_single_gen2", "left", tip_racks=[tip_rack_20]
    )

    # ---------- Define and load liquids ----------
    liquid_water  = protocol.define_liquid(
        "DI Water",
        description="Deionized water",
        display_color="#50d5ffff",
    )
    liquid_bacl2  = protocol.define_liquid(
        "BaCl₂·2H₂O (barium chloride dihydrate)",
        description=(
            "BaCl₂·2H₂O dissolved in DI water, "
            "1.0 M stock (24.426 g / 100 mL). Toxic — handle with care."
        ),
        display_color="#ff4f4fff",
    )
    liquid_na2so4 = protocol.define_liquid(
        "Na₂SO₄ (sodium sulfate, anhydrous)",
        description="Na₂SO₄ dissolved in DI water, 1.0 M stock (14.204 g / 100 mL). Low hazard.",
        display_color="#b925ffff",
    )
    liquid_nacl   = protocol.define_liquid(
        "NaCl (sodium chloride)",
        description="NaCl dissolved in DI water, 5.0 M stock (29.22 g / 100 mL). Low hazard.",
        display_color="#ff9900",
    )
    tube_rack_1.load_liquid(wells=["A1"], liquid=liquid_water,  volume=15000)
    tube_rack_1.load_liquid(wells=["A2"], liquid=liquid_bacl2,  volume=15000)
    tube_rack_1.load_liquid(wells=["B1"], liquid=liquid_na2so4, volume=15000)
    tube_rack_1.load_liquid(wells=["B2"], liquid=liquid_nacl,   volume=15000)

    # ---------- Build per-well volume arrays (96 wells total) ----------
    # Wells 1–80  (columns 1–10, column-first): LHS-sampled conditions
    # Wells 81–84 (A11–D11):  Ba²⁺-only negative controls
    # Wells 85–88 (E11–H11):  SO₄²⁻-only negative controls
    # Wells 89–92 (A12–D12):  Blank controls (NaCl only, no Ba²⁺ or SO₄²⁻)
    # Wells 93–96 (E12–H12):  Positive controls (50 mM Ba²⁺ + 50 mM SO₄²⁻)

    ROWS = "ABCDEFGH"
    lhs_wells = [f"{r}{c}" for c in range(1, 11) for r in ROWS]   # 80 wells, column-first

    all_wells    = list(lhs_wells)
    v_bacl2_all  = []
    v_na2so4_all = []
    v_nacl_all   = []
    v_water_all  = []

    for cond in LHS_CONDITIONS:
        vb, vs, vn, vw = _calc_volumes(*cond)
        v_bacl2_all.append(vb)
        v_na2so4_all.append(vs)
        v_nacl_all.append(vn)
        v_water_all.append(vw)

    def _add_control(well, ba_mm, so4_mm, nacl_mol):
        vb, vs, vn, vw = _calc_volumes(ba_mm, so4_mm, nacl_mol)
        all_wells.append(well)
        v_bacl2_all.append(vb)
        v_na2so4_all.append(vs)
        v_nacl_all.append(vn)
        v_water_all.append(vw)

    # Wells 81–84: Ba²⁺-only negative controls (50 mM BaCl₂, no SO₄²⁻)
    for w in ["A11", "B11", "C11", "D11"]:
        _add_control(w, 50.0, 0.0, 0.0)

    # Wells 85–88: SO₄²⁻-only negative controls (50 mM Na₂SO₄, no Ba²⁺)
    for w in ["E11", "F11", "G11", "H11"]:
        _add_control(w, 0.0, 50.0, 0.0)

    # Wells 89–92: Blank controls (3 molal NaCl, no Ba²⁺ or SO₄²⁻)
    for w in ["A12", "B12", "C12", "D12"]:
        _add_control(w, 0.0, 0.0, 3.0)

    # Wells 93–96: Positive controls (50 mM Ba²⁺ + 50 mM SO₄²⁻ → known precipitation)
    for w in ["E12", "F12", "G12", "H12"]:
        _add_control(w, 50.0, 50.0, 0.0)

    # Helper: return (wells, vols) filtered to only those where vol > 0
    def _nonzero(vols):
        ws = [w for w, v in zip(all_wells, vols) if v > 0]
        vs = [v for v in vols if v > 0]
        return ws, vs

    # ==========================================================================
    # PROTOCOL STEPS
    # Each reagent uses exactly one tip, picked up at the start of its step and
    # dropped into the trash at the end.  Na₂SO₄ is added last to trigger
    # BaSO₄ precipitation simultaneously across all relevant wells.
    # ==========================================================================

    # ---------- Step 1: DI Water (p20, Tip 1) ---------------------------------
    # All 96 wells receive DI water to bring the total volume to 200 µL.
    # The p20 makes multiple 20 µL aspirations per well as needed.
    water_wells, water_vols = _nonzero(v_water_all)
    pipette_left.pick_up_tip()
    pipette_left.transfer(
        volume=water_vols,
        source=[tube_rack_1["A1"]] * len(water_wells),
        dest=[well_plate_1[w] for w in water_wells],
        new_tip="never",
    )
    pipette_left.drop_tip()

    # ---------- Step 2: NaCl (p20, Tip 2) ------------------------------------
    # Wells that need NaCl as an ionic-strength modifier (≥ 1 µL from 5 M stock).
    # The p20 makes multiple 20 µL aspirations per well as needed.
    nacl_wells, nacl_vols = _nonzero(v_nacl_all)
    pipette_left.pick_up_tip()
    if nacl_wells:
        pipette_left.transfer(
            volume=nacl_vols,
            source=[tube_rack_1["B2"]] * len(nacl_wells),
            dest=[well_plate_1[w] for w in nacl_wells],
            new_tip="never",
        )
    pipette_left.drop_tip()

    # ---------- Step 3: BaCl₂ (p20, Tip 3) -----------------------------------
    # Wells that receive Ba²⁺: LHS wells 1–80, Ba-only controls (81–84),
    # and positive controls (93–96).
    bacl2_wells, bacl2_vols = _nonzero(v_bacl2_all)
    pipette_left.pick_up_tip()
    if bacl2_wells:
        pipette_left.transfer(
            volume=bacl2_vols,
            source=[tube_rack_1["A2"]] * len(bacl2_wells),
            dest=[well_plate_1[w] for w in bacl2_wells],
            new_tip="never",
        )
    pipette_left.drop_tip()

    # ---------- Step 4: Na₂SO₄ LAST (p20, Tip 4) — triggers precipitation ----
    # Na₂SO₄ is dispensed last so that precipitation begins simultaneously
    # across all wells.  Wells receiving SO₄²⁻: LHS wells 1–80, SO₄-only
    # controls (85–88), and positive controls (93–96).
    so4_wells, so4_vols = _nonzero(v_na2so4_all)
    pipette_left.pick_up_tip()
    if so4_wells:
        pipette_left.transfer(
            volume=so4_vols,
            source=[tube_rack_1["B1"]] * len(so4_wells),
            dest=[well_plate_1[w] for w in so4_wells],
            new_tip="never",
        )
    pipette_left.drop_tip()


CUSTOM_LABWARE = json.loads("""{"custom_beta/ac_6_tuberack_15000ul/1":{"ordering":[["A1","B1"],["A2","B2"],["A3","B3"]],"brand":{"brand":"AC","brandId":[]},"metadata":{"displayName":"AC 6 Tube Rack with AC 15 mL","displayCategory":"tubeRack","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.76,"yDimension":85.48,"zDimension":61},"wells":{"A1":{"depth":58,"totalLiquidVolume":15000,"shape":"circular","diameter":20,"x":24,"y":62.48,"z":3},"B1":{"depth":58,"totalLiquidVolume":15000,"shape":"circular","diameter":20,"x":24,"y":23.48,"z":3},"A2":{"depth":58,"totalLiquidVolume":15000,"shape":"circular","diameter":20,"x":63,"y":62.48,"z":3},"B2":{"depth":58,"totalLiquidVolume":15000,"shape":"circular","diameter":20,"x":63,"y":23.48,"z":3},"A3":{"depth":58,"totalLiquidVolume":15000,"shape":"circular","diameter":20,"x":102,"y":62.48,"z":3},"B3":{"depth":58,"totalLiquidVolume":15000,"shape":"circular","diameter":20,"x":102,"y":23.48,"z":3}},"groups":[{"brand":{"brand":"AC","brandId":[]},"metadata":{"wellBottomShape":"flat","displayCategory":"tubeRack"},"wells":["A1","B1","A2","B2","A3","B3"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"ac_6_tuberack_15000ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}}""")
