"""A simulation-only check of the 11-06 deck (not the plate A protocol):

    opentrons_simulate -L byuvcl_6_vialholder_20ml check_deck.py      # opentrons 8.x; 10.x no longer simulates OT-2

Heater-shaker with its 96 Flat Bottom Adapter and the NEST plate in slot 7, the two vial holders in slots 4 and 5,
300 uL tips in slot 6, the P300 single on the left. One transfer from each kind of stock into A1.
"""
from opentrons import protocol_api

metadata = {"apiLevel": "2.15", "protocolName": "BaSO4 deck check: vial holders and heater-shaker"}


def run(protocol: protocol_api.ProtocolContext):
    hs = protocol.load_module("heaterShakerModuleV1", 7)
    plate = hs.load_adapter("opentrons_96_flat_bottom_adapter").load_labware("nest_96_wellplate_200ul_flat")
    barium = protocol.load_labware("byuvcl_6_vialholder_20ml", 4, namespace="custom_beta")
    rest = protocol.load_labware("byuvcl_6_vialholder_20ml", 5, namespace="custom_beta")
    p300 = protocol.load_instrument("p300_single_gen2", "left",
                                    tip_racks=[protocol.load_labware("opentrons_96_tiprack_300ul", 6)])
    hs.close_labware_latch()
    p300.transfer(150, rest["B3"], plate["A1"])                        # DI water
    p300.transfer(40, rest["B2"], plate["A1"])                         # 5 M NaCl
    p300.transfer(20, barium["A3"], plate["A1"])                       # 1 mM barium chloride
    p300.transfer(20, rest["A3"], plate["A1"].top(2))                  # 1 mM sodium sulfate, last, from above
    protocol.comment(f"plate A1 top: {plate['A1'].top().point}; 0.1 M barium vial bottom: {barium['A1'].bottom().point}")
