import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "Experiment 1 - AgCl Precipitation",
    "description": "First experiment on OT-2, created 3/4/26 | AgNO₃ + NaCl → AgCl ↓ + NaNO₃ ",
    "created": "2026-03-04T17:00:55.572Z",
    "internalAppBuildDate": "Thu, 19 Feb 2026 15:56:59 GMT",
    "lastModified": "2026-03-04T17:32:48.196Z",
    "protocolDesigner": "8.8.1",
    "source": "Protocol Designer",
}

requirements = {"robotType": "OT-2", "apiLevel": "2.27"}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Modules:
    temperature_module_1 = protocol.load_module("temperatureModuleV2", "9")

    # Load Labware:
    tip_rack_1 = protocol.load_labware(
        "opentrons_96_filtertiprack_20ul",
        location="2",
        namespace="opentrons",
        version=1,
    )
    tube_rack_1 = protocol.load_labware_from_definition(
        CUSTOM_LABWARE["custom_beta/ac_6_tuberack_15000ul/1"],
        location="5",
    )
    well_plate_1 = protocol.load_labware(
        "corning_96_wellplate_360ul_flat",
        location="4",
        namespace="opentrons",
        version=5,
    )

    # Load Pipettes:
    pipette_left = protocol.load_instrument("p20_single_gen2", "left")

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "DI Water",
        description="Deionized water",
        display_color="#50d5ffff",
    )
    liquid_2 = protocol.define_liquid(
        "BaCl₂·2H₂O (barium chloride dihydrate)",
        description="BaCl₂·2H₂O (barium chloride dihydrate, or BaCl2 dissolved in DI water), Initial Concentration: 24.426 g/100mL, Toxic (ingestion, inhalation)",
        display_color="#ff4f4fff",
    )
    liquid_3 = protocol.define_liquid(
        "Na₂SO₄ (sodium sulfate, anhydrous)",
        description="Na₂SO₄ (sodium sulfate, anhydrous), Initial Concentration: 14.204 g / 100 mL, low hazard",
        display_color="#b925ffff",
    )
    liquid_4 = protocol.define_liquid(
        "NaCl (sodium chloride)",
        description="NaCl (sodium chloride), Initial Concentration: 29.22 g / 100 mL, low hazard",
        display_color="#ff9900",
    )

    # Load Liquids:
    tube_rack_1.load_liquid(
        wells=["A1"],
        liquid=liquid_1,
        volume=15000,
    )
    tube_rack_1.load_liquid(
        wells=["A2"],
        liquid=liquid_2,
        volume=15000,
    )
    tube_rack_1.load_liquid(
        wells=["B1"],
        liquid=liquid_3,
        volume=15000,
    )
    tube_rack_1.load_liquid(
        wells=["B2"],
        liquid=liquid_4,
        volume=15000,
    )

    # PROTOCOL STEPS

    # Step 1: transfer
    pipette_left.distribute_with_liquid_class(
        volume=10,
        source=[tube_rack_1["A1"]],
        dest=[well_plate_1["A1"], well_plate_1["B1"], well_plate_1["C1"], well_plate_1["D1"], well_plate_1["E1"], well_plate_1["F1"], well_plate_1["G1"], well_plate_1["H1"], well_plate_1["A2"], well_plate_1["B2"], well_plate_1["C2"], well_plate_1["D2"], well_plate_1["E2"], well_plate_1["F2"], well_plate_1["G2"], well_plate_1["H2"], well_plate_1["A3"], well_plate_1["B3"], well_plate_1["C3"], well_plate_1["D3"], well_plate_1["E3"], well_plate_1["F3"], well_plate_1["G3"], well_plate_1["H3"], well_plate_1["A4"], well_plate_1["B4"], well_plate_1["C4"], well_plate_1["D4"], well_plate_1["E4"], well_plate_1["F4"], well_plate_1["G4"], well_plate_1["H4"], well_plate_1["A5"], well_plate_1["B5"], well_plate_1["C5"], well_plate_1["D5"], well_plate_1["E5"], well_plate_1["F5"], well_plate_1["G5"], well_plate_1["H5"], well_plate_1["A6"], well_plate_1["B6"], well_plate_1["C6"], well_plate_1["D6"], well_plate_1["E6"], well_plate_1["F6"], well_plate_1["G6"], well_plate_1["H6"], well_plate_1["A7"], well_plate_1["B7"], well_plate_1["C7"], well_plate_1["D7"], well_plate_1["E7"], well_plate_1["F7"], well_plate_1["G7"], well_plate_1["H7"], well_plate_1["A8"], well_plate_1["B8"], well_plate_1["C8"], well_plate_1["D8"], well_plate_1["E8"], well_plate_1["F8"], well_plate_1["G8"], well_plate_1["H8"], well_plate_1["A9"], well_plate_1["B9"], well_plate_1["C9"], well_plate_1["D9"], well_plate_1["E9"], well_plate_1["F9"], well_plate_1["G9"], well_plate_1["H9"], well_plate_1["A10"], well_plate_1["B10"], well_plate_1["C10"], well_plate_1["D10"], well_plate_1["E10"], well_plate_1["F10"], well_plate_1["G10"], well_plate_1["H10"], well_plate_1["A11"], well_plate_1["B11"], well_plate_1["C11"], well_plate_1["D11"], well_plate_1["E11"], well_plate_1["F11"], well_plate_1["G11"], well_plate_1["H11"], well_plate_1["A12"], well_plate_1["B12"], well_plate_1["C12"], well_plate_1["D12"], well_plate_1["E12"], well_plate_1["F12"], well_plate_1["G12"], well_plate_1["H12"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_1",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 0)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

CUSTOM_LABWARE = json.loads("""{"custom_beta/ac_6_tuberack_15000ul/1":{"ordering":[["A1","B1"],["A2","B2"],["A3","B3"]],"brand":{"brand":"AC","brandId":[]},"metadata":{"displayName":"AC 6 Tube Rack with AC 15 mL","displayCategory":"tubeRack","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.76,"yDimension":85.48,"zDimension":61},"wells":{"A1":{"depth":58,"totalLiquidVolume":15000,"shape":"circular","diameter":20,"x":24,"y":62.48,"z":3},"B1":{"depth":58,"totalLiquidVolume":15000,"shape":"circular","diameter":20,"x":24,"y":23.48,"z":3},"A2":{"depth":58,"totalLiquidVolume":15000,"shape":"circular","diameter":20,"x":63,"y":62.48,"z":3},"B2":{"depth":58,"totalLiquidVolume":15000,"shape":"circular","diameter":20,"x":63,"y":23.48,"z":3},"A3":{"depth":58,"totalLiquidVolume":15000,"shape":"circular","diameter":20,"x":102,"y":62.48,"z":3},"B3":{"depth":58,"totalLiquidVolume":15000,"shape":"circular","diameter":20,"x":102,"y":23.48,"z":3}},"groups":[{"brand":{"brand":"AC","brandId":[]},"metadata":{"wellBottomShape":"flat","displayCategory":"tubeRack"},"wells":["A1","B1","A2","B2","A3","B3"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"ac_6_tuberack_15000ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}}""")

DESIGNER_APPLICATION = """{"robot":{"model":"OT-2 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.8.0","data":{"pipetteTiprackAssignments":{"363b3fde-2ad0-4294-8a7c-d8732f8fc287":["opentrons/opentrons_96_filtertiprack_20ul/1"]},"dismissedWarnings":{"form":[],"timeline":[]},"ingredients":{"0":{"displayName":"DI Water","displayColor":"#50d5ffff","description":"Deionized water","liquidGroupId":"0"},"1":{"displayName":"BaCl₂·2H₂O (barium chloride dihydrate)","displayColor":"#ff4f4fff","description":"BaCl₂·2H₂O (barium chloride dihydrate, or BaCl2 dissolved in DI water), Initial Concentration: 24.426 g/100mL, Toxic (ingestion, inhalation)","liquidGroupId":"1"},"2":{"displayName":"Na₂SO₄ (sodium sulfate, anhydrous)","displayColor":"#b925ffff","description":"Na₂SO₄ (sodium sulfate, anhydrous), Initial Concentration: 14.204 g / 100 mL, low hazard","liquidGroupId":"2"},"3":{"displayName":"NaCl (sodium chloride)","displayColor":"#ff9900","description":"NaCl (sodium chloride), Initial Concentration: 29.22 g / 100 mL, low hazard","liquidGroupId":"3"}},"ingredLocations":{"a5140331-be77-469c-accb-fa778ad1dd5b:custom_beta/ac_6_tuberack_15000ul/1":{"A1":{"0":{"volume":15000}},"A2":{"1":{"volume":15000}},"B1":{"2":{"volume":15000}},"B2":{"3":{"volume":15000}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__","labwareLocationUpdate":{"5c6e75c7-c528-4d46-978d-1429c5b1008c:opentrons/opentrons_96_filtertiprack_20ul/1":"2","a5140331-be77-469c-accb-fa778ad1dd5b:custom_beta/ac_6_tuberack_15000ul/1":"5","02e66b75-3732-42f9-8fdb-3baa4d1e1732:opentrons/corning_96_wellplate_360ul_flat/5":"4"},"pipetteLocationUpdate":{"363b3fde-2ad0-4294-8a7c-d8732f8fc287":"left"},"moduleLocationUpdate":{"08451926-7248-44df-8228-b33b57b9bbb1:temperatureModuleType":"9"},"moduleStateUpdate":{},"trashBinLocationUpdate":{"128735c1-b19d-4258-80c4-6f86898f8fd8:trashBin":"cutout12"},"wasteChuteLocationUpdate":{},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{}},"915ca1f0-f82f-4266-b692-a070cd43a1d9":{"id":"915ca1f0-f82f-4266-b692-a070cd43a1d9","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"3.7","aspirate_labware":"a5140331-be77-469c-accb-fa778ad1dd5b:custom_beta/ac_6_tuberack_15000ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"3.7","blowout_location":"source_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"3.7","dispense_labware":"02e66b75-3732-42f9-8fdb-3baa4d1e1732:opentrons/corning_96_wellplate_360ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"0","dropTip_location":"128735c1-b19d-4258-80c4-6f86898f8fd8:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"363b3fde-2ad0-4294-8a7c-d8732f8fc287","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10"}},"orderedStepIds":["915ca1f0-f82f-4266-b692-a070cd43a1d9"],"pipettes":{"363b3fde-2ad0-4294-8a7c-d8732f8fc287":{"pipetteName":"p20_single_gen2"}},"modules":{"08451926-7248-44df-8228-b33b57b9bbb1:temperatureModuleType":{"model":"temperatureModuleV2"}},"labware":{"5c6e75c7-c528-4d46-978d-1429c5b1008c:opentrons/opentrons_96_filtertiprack_20ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 20 µL","labwareDefURI":"opentrons/opentrons_96_filtertiprack_20ul/1"},"a5140331-be77-469c-accb-fa778ad1dd5b:custom_beta/ac_6_tuberack_15000ul/1":{"displayName":"AC 6 Tube Rack with AC 15 mL","labwareDefURI":"custom_beta/ac_6_tuberack_15000ul/1"},"02e66b75-3732-42f9-8fdb-3baa4d1e1732:opentrons/corning_96_wellplate_360ul_flat/5":{"displayName":"Corning 96 Well Plate 360 µL Flat","labwareDefURI":"opentrons/corning_96_wellplate_360ul_flat/5"}}}},"metadata":{"protocolName":"Experiment 1 - AgCl Precipitation","author":"","description":"First experiment on OT-2, created 3/4/26 | AgNO₃ + NaCl → AgCl ↓ + NaNO₃ ","source":"Protocol Designer","created":1772643655572,"lastModified":1772645568196}}"""
