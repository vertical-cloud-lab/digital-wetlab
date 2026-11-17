"""Plate A of the barium sulfate SOP (PR 84): 84 wells of barium chloride and sodium sulfate, sulfate last.

Run it from the Opentrons App: Protocols > Import this one file. The vial holder's labware definition
is inside it, so there is nothing else to import. Then Labware Position Check, then Start.

Deck (as in docs/baso4-sop-3d/README.md):
  7   Heater-Shaker with its 96 Flat Bottom Adapter and the NEST 96 flat 200 uL plate (black paper under it)
  4   vial holder, barium chloride: A1 0.1 M, A2 10 mM, A3 1 mM, B1 0.1 mM (B2 and B3 empty)
  5   vial holder: sodium sulfate A1 0.1 M, A2 10 mM, A3 1 mM, B1 0.1 mM; B2 5 M NaCl; B3 DI water
  6   Opentrons 96 tip rack, 300 uL, FULL (78 tips are used)
  12  trash
  P300 single GEN2 on the left mount. All ten vials UNCAPPED. Nothing in slot 8 or slot 10 (the path from the plate
  to the trash passes the corner of slot 10, and the robot doesn't know about anything not listed here).

What the robot does:
  1. pauses so you can check the deck, until you press Resume;
  2. turns the rail lights on and closes the Heater-Shaker's latch (no heating, no shaking). If the plate is
     straight on the deck instead, set "Plate on the Heater-Shaker" to off in the App's parameters;
  3. DI water into 84 wells (one tip);
  4. 40 uL of 5 M NaCl into 64 wells (one tip);
  5. barium chloride into 72 wells (one tip per vial);
  6. sodium sulfate into 72 wells, last, with a new tip for every well, then (by default) mixes
     each well gently with that tip. A comment "SULFATE <well>" in the run log marks each well's start;
  7. the run ends and the pipette parks at the back right. Then seal the plate and set up the phone.

Every well ends at 200 uL. Every dose is 20, 40 or 60 uL, so nothing falls below the P300's 20 uL.
The tip never goes deeper into a vial than 46.5 mm below its rim (7 mm above the vial's inside floor),
and it follows each vial's level down as the robot draws from it.
"""
import json
import math

from opentrons import protocol_api

metadata = {
    "protocolName": "BaSO4 plate A (PR 84): 84 wells, sulfate last",
    "author": "BYU VCL, digital-wetlab PR 84",
    "description": "Barium chloride and sodium sulfate at 0.01, 0.1, 1 and 3 mM each, with and without 1 M NaCl, "
                   "blanks and 10 mM controls. Stocks in two printed 6-vial holders (slots 4 and 5), plate on the "
                   "Heater-Shaker in slot 7 (not heated or shaken).",
}
requirements = {"robotType": "OT-2", "apiLevel": "2.20"}

# The printed holder (docs/baso4-sop-3d/cad/byuvcl_6_vialholder_20ml/1.json), uncapped 27 x 55 mm vials.
HOLDER_DEF = json.loads('{"ordering":[["A1","B1"],["A2","B2"],["A3","B3"]],"brand":{"brand":"BYU Vertical Cloud Lab","brandId":["byuvcl_6_vialholder_20ml"]},"metadata":{"displayName":"BYU VCL 6-vial holder, 20 mL VOA vials (27 x 55 mm), uncapped","displayCategory":"tubeRack","displayVolumeUnits":"mL","tags":[]},"dimensions":{"xDimension":127.76,"yDimension":85.48,"zDimension":58.0},"wells":{"A1":{"depth":53.5,"totalLiquidVolume":20000,"shape":"circular","diameter":20.0,"x":23.88,"y":62.74,"z":4.5},"A2":{"depth":53.5,"totalLiquidVolume":20000,"shape":"circular","diameter":20.0,"x":63.88,"y":62.74,"z":4.5},"A3":{"depth":53.5,"totalLiquidVolume":20000,"shape":"circular","diameter":20.0,"x":103.88,"y":62.74,"z":4.5},"B1":{"depth":53.5,"totalLiquidVolume":20000,"shape":"circular","diameter":20.0,"x":23.88,"y":22.74,"z":4.5},"B2":{"depth":53.5,"totalLiquidVolume":20000,"shape":"circular","diameter":20.0,"x":63.88,"y":22.74,"z":4.5},"B3":{"depth":53.5,"totalLiquidVolume":20000,"shape":"circular","diameter":20.0,"x":103.88,"y":22.74,"z":4.5}},"groups":[{"metadata":{"displayName":"20 mL VOA vials","displayCategory":"tubeRack","wellBottomShape":"flat"},"brand":{"brand":"Fisher Scientific","brandId":["12-100-112"]},"wells":["A1","B1","A2","B2","A3","B3"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"byuvcl_6_vialholder_20ml"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}')

# Plate A: one shuffle (the SOP animation's, seed 80). (well, Ba mM, SO4 mM, NaCl 1 = 1 M / 0 = none, role)
PLATE_MAP = [
    ("A1", 3.0, 0.1, 1, "pair, NaCl, rep 1"),
    ("B1", 0.1, 0.01, 0, "pair, no NaCl"),
    ("C1", 0.0, 0.1, 1, "sulfate only"),
    ("E1", 3.0, 3.0, 1, "pair, NaCl, rep 1"),
    ("F1", 0.0, 0.0, 1, "NaCl blank"),
    ("G1", 0.01, 0.1, 1, "pair, NaCl, rep 1"),
    ("H1", 0.01, 0.01, 1, "pair, NaCl, rep 1"),
    ("A2", 3.0, 0.01, 1, "pair, NaCl, rep 1"),
    ("B2", 1.0, 0.01, 1, "pair, NaCl, rep 1"),
    ("C2", 1.0, 1.0, 1, "pair, NaCl, rep 1"),
    ("E2", 3.0, 0.0, 1, "barium only"),
    ("F2", 0.01, 0.01, 1, "pair, NaCl, rep 2"),
    ("G2", 3.0, 1.0, 1, "pair, NaCl, rep 1"),
    ("H2", 0.0, 0.0, 0, "water blank"),
    ("A3", 1.0, 0.1, 0, "pair, no NaCl"),
    ("B3", 0.1, 1.0, 1, "pair, NaCl, rep 1"),
    ("D3", 0.0, 0.0, 1, "NaCl blank"),
    ("E3", 0.1, 1.0, 0, "pair, no NaCl"),
    ("G3", 0.1, 0.01, 1, "pair, NaCl, rep 1"),
    ("H3", 3.0, 0.1, 1, "pair, NaCl, rep 2"),
    ("A4", 0.01, 0.1, 1, "pair, NaCl, rep 2"),
    ("B4", 0.01, 0.1, 0, "pair, no NaCl"),
    ("C4", 1.0, 1.0, 1, "pair, NaCl, rep 2"),
    ("E4", 1.0, 3.0, 1, "pair, NaCl, rep 1"),
    ("F4", 3.0, 3.0, 1, "pair, NaCl, rep 2"),
    ("G4", 1.0, 0.01, 1, "pair, NaCl, rep 2"),
    ("H4", 0.01, 1.0, 1, "pair, NaCl, rep 1"),
    ("A5", 0.0, 0.01, 1, "sulfate only"),
    ("B5", 3.0, 1.0, 1, "pair, NaCl, rep 2"),
    ("C5", 3.0, 0.01, 1, "pair, NaCl, rep 2"),
    ("D5", 10.0, 10.0, 1, "positive control"),
    ("E5", 1.0, 1.0, 0, "pair, no NaCl"),
    ("F5", 0.01, 3.0, 1, "pair, NaCl, rep 1"),
    ("G5", 3.0, 3.0, 1, "pair, NaCl, rep 3"),
    ("H5", 1.0, 0.01, 0, "pair, no NaCl"),
    ("A6", 3.0, 3.0, 0, "pair, no NaCl"),
    ("B6", 3.0, 0.1, 0, "pair, no NaCl"),
    ("C6", 0.0, 0.0, 0, "water blank"),
    ("D6", 1.0, 3.0, 1, "pair, NaCl, rep 2"),
    ("E6", 0.01, 3.0, 1, "pair, NaCl, rep 2"),
    ("F6", 1.0, 0.01, 1, "pair, NaCl, rep 3"),
    ("G6", 0.01, 1.0, 1, "pair, NaCl, rep 2"),
    ("H6", 3.0, 0.01, 0, "pair, no NaCl"),
    ("A7", 0.1, 3.0, 1, "pair, NaCl, rep 1"),
    ("B7", 0.1, 0.1, 1, "pair, NaCl, rep 1"),
    ("C7", 10.0, 10.0, 1, "positive control"),
    ("D7", 0.01, 0.01, 1, "pair, NaCl, rep 3"),
    ("E7", 0.1, 0.1, 1, "pair, NaCl, rep 2"),
    ("F7", 0.01, 0.0, 1, "barium only"),
    ("H7", 0.0, 0.0, 0, "water blank"),
    ("B8", 0.1, 3.0, 1, "pair, NaCl, rep 2"),
    ("C8", 0.1, 3.0, 1, "pair, NaCl, rep 3"),
    ("D8", 0.01, 1.0, 0, "pair, no NaCl"),
    ("E8", 0.0, 3.0, 1, "sulfate only"),
    ("F8", 1.0, 0.1, 1, "pair, NaCl, rep 1"),
    ("G8", 10.0, 10.0, 1, "positive control"),
    ("H8", 0.1, 0.1, 1, "pair, NaCl, rep 3"),
    ("A9", 10.0, 10.0, 1, "positive control"),
    ("B9", 0.01, 3.0, 0, "pair, no NaCl"),
    ("C9", 0.01, 1.0, 1, "pair, NaCl, rep 3"),
    ("D9", 0.0, 0.0, 1, "NaCl blank"),
    ("E9", 0.1, 0.01, 1, "pair, NaCl, rep 2"),
    ("F9", 1.0, 0.0, 1, "barium only"),
    ("G9", 0.0, 0.0, 0, "water blank"),
    ("H9", 1.0, 0.1, 1, "pair, NaCl, rep 2"),
    ("B10", 1.0, 3.0, 1, "pair, NaCl, rep 3"),
    ("C10", 0.01, 0.1, 1, "pair, NaCl, rep 3"),
    ("D10", 3.0, 0.1, 1, "pair, NaCl, rep 3"),
    ("E10", 0.1, 1.0, 1, "pair, NaCl, rep 2"),
    ("F10", 0.01, 3.0, 1, "pair, NaCl, rep 3"),
    ("G10", 0.0, 0.0, 1, "NaCl blank"),
    ("H10", 0.0, 1.0, 1, "sulfate only"),
    ("A11", 0.1, 0.01, 1, "pair, NaCl, rep 3"),
    ("B11", 0.1, 0.1, 0, "pair, no NaCl"),
    ("D11", 3.0, 1.0, 1, "pair, NaCl, rep 3"),
    ("E11", 1.0, 0.1, 1, "pair, NaCl, rep 3"),
    ("F11", 0.1, 3.0, 0, "pair, no NaCl"),
    ("G11", 3.0, 0.01, 1, "pair, NaCl, rep 3"),
    ("H11", 0.1, 0.0, 1, "barium only"),
    ("B12", 1.0, 3.0, 0, "pair, no NaCl"),
    ("C12", 0.01, 0.01, 0, "pair, no NaCl"),
    ("D12", 3.0, 1.0, 0, "pair, no NaCl"),
    ("F12", 1.0, 1.0, 1, "pair, NaCl, rep 3"),
    ("H12", 0.1, 1.0, 1, "pair, NaCl, rep 3"),
]

WELL_UL = 200.0
NACL_UL = 40.0                      # 40 uL of 5 M in 200 uL: 1.0 M
# Final concentration (mM) -> (stock, uL). 20 uL of a stock gives a tenth of it; 60 uL of 10 mM gives 3 mM.
DOSE = {0.01: ("0.1 mM", 20.0), 0.1: ("1 mM", 20.0), 1.0: ("10 mM", 20.0), 3.0: ("10 mM", 60.0),
        10.0: ("0.1 M", 20.0)}

# Where each stock is: (slot, well). The barium holder's B2 and B3 stay empty.
VIALS = {
    ("ba", "0.1 M"): (4, "A1"), ("ba", "10 mM"): (4, "A2"), ("ba", "1 mM"): (4, "A3"), ("ba", "0.1 mM"): (4, "B1"),
    ("so", "0.1 M"): (5, "A1"), ("so", "10 mM"): (5, "A2"), ("so", "1 mM"): (5, "A3"), ("so", "0.1 mM"): (5, "B1"),
    ("nacl", "5 M"): (5, "B2"), ("water", ""): (5, "B3"),
}
# What the protocol assumes is in each vial at the start (uL). Deliberately about 1 mL LESS than the SOP makes
# (13.5-15 mL), so the tip goes a little deeper than it needs to, never shallower. DI water: the SOP's 15 g minus 1.
START_UL = {
    ("ba", "0.1 M"): 12500.0, ("ba", "10 mM"): 12500.0, ("ba", "1 mM"): 12500.0, ("ba", "0.1 mM"): 14000.0,
    ("so", "0.1 M"): 12500.0, ("so", "10 mM"): 12500.0, ("so", "1 mM"): 12500.0, ("so", "0.1 mM"): 14000.0,
    ("nacl", "5 M"): 14000.0, ("water", ""): 14000.0,
}
VIAL_AREA = math.pi * (24.6 / 2) ** 2      # mm^2 inside a 27 mm vial (1.2 mm glass): 1 mL = 2.1 mm of height
TIP_FLOOR = 7.0     # mm above a vial's inside floor: the deepest the tip goes (46.5 mm below the rim)
TIP_UNDER = 2.5     # mm below the vial's computed surface, where the tip aspirates
MIN_COVER = 1.0     # the computed surface must stay at least this far above the tip, or the protocol refuses to run
WELL_AREA = math.pi * (6.85 / 2) ** 2      # mm^2, NEST 96 flat 200 uL: 1 uL = 0.027 mm


def add_parameters(parameters):
    parameters.add_bool(
        variable_name="on_heater_shaker",
        display_name="Plate on the Heater-Shaker",
        description="On: plate on the Heater-Shaker's 96 Flat Bottom Adapter in slot 7. Off: plate right on slot 7.",
        default=True,
    )
    parameters.add_bool(
        variable_name="mix_after_sulfate",
        display_name="Mix after the sulfate",
        description="On: 3 gentle 80 uL mixes in each well with its sulfate tip. Off: dispense from above, no mixing.",
        default=True,
    )


def wells_needing(kind):
    """Wells that get this liquid, in column order (A1, B1 ... H1, A2 ...), with (stock, uL)."""
    out = []
    for well, ba, so, nacl, _role in PLATE_MAP:
        if kind == "water":
            out.append((well, ("water", ""), water_ul(ba, so, nacl)))
        elif kind == "nacl" and nacl:
            out.append((well, ("nacl", "5 M"), NACL_UL))
        elif kind in ("ba", "so"):
            c = ba if kind == "ba" else so
            if c:
                stock, ul = DOSE[c]
                out.append((well, (kind, stock), ul))
    return out


def water_ul(ba, so, nacl):
    used = (NACL_UL if nacl else 0.0) + (DOSE[ba][1] if ba else 0.0) + (DOSE[so][1] if so else 0.0)
    return WELL_UL - used


def run(protocol: protocol_api.ProtocolContext):
    mix = protocol.params.mix_after_sulfate

    # ---- deck
    if protocol.params.on_heater_shaker:
        hs = protocol.load_module("heaterShakerModuleV1", 7)
        adapter = hs.load_adapter("opentrons_96_flat_bottom_adapter")
        plate = adapter.load_labware("nest_96_wellplate_200ul_flat", label="plate A (black paper under it)")
    else:
        hs = None
        plate = protocol.load_labware("nest_96_wellplate_200ul_flat", 7, label="plate A (black paper under it)")
    holders = {4: protocol.load_labware_from_definition(HOLDER_DEF, 4, label="barium chloride vials"),
               5: protocol.load_labware_from_definition(HOLDER_DEF, 5, label="sulfate, NaCl and water vials")}
    tips = protocol.load_labware("opentrons_96_tiprack_300ul", 6)
    p300 = protocol.load_instrument("p300_single_gen2", "left", tip_racks=[tips])
    p300.flow_rate.aspirate = 46.43          # half the default: slower draws are more accurate
    p300.flow_rate.dispense = 92.86
    p300.flow_rate.blow_out = 92.86

    def vial(key):
        slot, name = VIALS[key]
        return holders[slot][name]

    # ---- liquids, so the App's deck map shows what goes where
    colours = {"ba": "#d62728", "so": "#1f77b4", "nacl": "#ff7f0e", "water": "#17becf"}
    names = {"ba": "barium chloride", "so": "sodium sulfate", "nacl": "sodium chloride", "water": "DI water"}
    for key in VIALS:
        kind, stock = key
        label = f"{names[kind]} {stock}".strip()
        liq = protocol.define_liquid(name=label, description=f"vial in slot {VIALS[key][0]}, {VIALS[key][1]}",
                                     display_color=colours[kind])
        vial(key).load_liquid(liquid=liq, volume=START_UL[key])

    # ---- check that every vial lasts, before anything moves
    level = dict(START_UL)
    for kind in ("water", "nacl", "ba", "so"):
        for _well, key, ul in wells_needing(kind):
            level[key] -= ul
            surf = level[key] / VIAL_AREA
            if surf < TIP_FLOOR + MIN_COVER:
                raise ValueError(f"not enough in the {key} vial: it would fall to {level[key] / 1000:.1f} mL")
    n_tips = 2 + len({key for _w, key, _ul in wells_needing("ba")}) + len(wells_needing("so"))
    if n_tips > 96:
        raise ValueError(f"{n_tips} tips needed, one rack holds 96")
    protocol.comment(f"Uses {n_tips} tips, from A1 of a full rack in slot 6.")

    level = dict(START_UL)
    in_well = {w: 0.0 for w, *_ in PLATE_MAP}

    def aspirate(ul, key):
        level[key] -= ul
        surf = level[key] / VIAL_AREA                    # mm above the vial's floor, after this draw
        z = max(TIP_FLOOR, surf - TIP_UNDER)
        p300.aspirate(ul, vial(key).bottom(z))
        protocol.delay(seconds=0.5)                      # let the liquid catch up with the plunger
        p300.move_to(vial(key).bottom(surf + 6), speed=15)   # leave the liquid slowly, so less clings to the tip

    def dispense(ul, well, blow_out=True):
        w = plate[well]
        in_well[well] += ul
        z = min(max(in_well[well] / WELL_AREA + 1.0, 1.0), w.depth - 1.0)   # 1 mm above the liquid it makes
        p300.dispense(ul, w.bottom(z))
        if blow_out:
            p300.blow_out(w.top(-1))                     # above the liquid, so no bubbles

    # ---- 1. check, then start
    where = "on the Heater-Shaker in slot 7" if hs else "in slot 7"
    protocol.pause(f"Check before Resume: all 10 vials uncapped; a FULL 300 uL tip rack in slot 6; the plate {where} "
                   "with A1 at the back left; nothing in slots 8 and 10; hands out." + (" Resume closes the latch." if hs else ""))
    protocol.set_rail_lights(True)
    if hs:
        hs.close_labware_latch()                         # no heating, no shaking: it only holds the plate

    # ---- 2. water, then NaCl: one tip each. The wells have nothing but water and NaCl at this point.
    for kind, what in (("water", "DI water"), ("nacl", "5 M NaCl, 40 uL")):
        todo = wells_needing(kind)
        protocol.comment(f"{what} into {len(todo)} wells")
        p300.pick_up_tip()
        for well, key, ul in todo:
            aspirate(ul, key)
            dispense(ul, well)
        p300.drop_tip()

    # ---- 3. barium chloride: one tip per vial, never into a sulfate vial
    todo = wells_needing("ba")
    protocol.comment(f"barium chloride into {len(todo)} wells")
    for stock in ("0.1 mM", "1 mM", "10 mM", "0.1 M"):
        mine = [t for t in todo if t[1] == ("ba", stock)]
        if not mine:
            continue
        p300.pick_up_tip()
        for well, key, ul in mine:
            aspirate(ul, key)
            dispense(ul, well)
        p300.drop_tip()

    # ---- 4. sodium sulfate, last: a new tip for every well, so no tip that touched barium goes into a stock
    todo = wells_needing("so")
    protocol.comment(f"sodium sulfate into {len(todo)} wells, last, a new tip each" + (", mixed" if mix else ""))
    for well, key, ul in todo:
        p300.pick_up_tip()
        aspirate(ul, key)
        protocol.comment(f"SULFATE {well}: {ul:.0f} uL of {key[1]}")
        dispense(ul, well, blow_out=not mix)
        if mix:
            p300.mix(3, 80, plate[well].bottom(1.0), rate=0.75)   # 1 mm off the floor: 35 uL/s up, 70 down
            p300.blow_out(plate[well].top(-1))
        p300.drop_tip()

    bad = [w for w, v in in_well.items() if abs(v - WELL_UL) > 1e-6]
    if bad:
        raise ValueError(f"wells not at 200 uL: {bad}")
    protocol.comment("Plate A is filled. When the run says completed: seal the plate, then set up the phone.")
