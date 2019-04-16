# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning enums that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not codegen enums associated with P2P or External Calibration since neither 
# are supported in Python
enums_codegen_method = {
    'CalADCInput': { 'codegen_method': 'no', },  # Calibration Enum - not supported in Python
}

enums_override_values = {
    'ReferenceClockSource': { 'values': {
        0: { 'name': 'NIFGEN_VAL_CLOCK_IN', },
        1: { 'name': 'NIFGEN_VAL_NONE', },
        2: { 'name': 'NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK', },
        3: { 'name': 'NIFGEN_VAL_PXI_CLOCK', },
        4: { 'name': 'NIFGEN_VAL_RTSI_7', },
    }, },
    'SampleClockSource': { 'values': {
        0: { 'name': 'NIFGEN_VAL_CLOCK_IN', },
        1: { 'name': 'NIFGEN_VAL_DDC_CLOCK_IN', },
        2: { 'name': 'NIFGEN_VAL_ONBOARD_CLOCK', },
        3: { 'name': 'NIFGEN_VAL_PXI_STAR_LINE', },
        4: { 'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_0_RTSI_0', },
        5: { 'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_1_RTSI_1', },
        6: { 'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_2_RTSI_2', },
        7: { 'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_3_RTSI_3', },
        8: { 'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_4_RTSI_4', },
        9: { 'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_5_RTSI_5', },
        10: { 'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_6_RTSI_6', },
        11: { 'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_7_RTSI_7', },
    }, },
    'SampleClockTimebaseSource': { 'values': {
        0: { 'name': 'NIFGEN_VAL_CLOCK_IN', },
        1: { 'name': 'NIFGEN_VAL_ONBOARD_CLOCK', },
    }, },
    'MarkerEventOutputBehavior': { 'values': {
        2: { 'name': 'NIFGEN_VAL_TOGGLE', },
    }, },
}

enums_additional_enums = {
    'RelativeTo': {
        'values': [
            {
                'name': 'NIFGEN_VAL_WAVEFORM_POSITION_START',
                'value': 0,
            },
            {
                'name': 'NIFGEN_VAL_WAVEFORM_POSITION_CURRENT',
                'value': 1,
            },
        ],
    },
    'TriggerWhen': {
        'values': [
            {
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101,
            },
            {
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102,
            },
        ],
    },
    'ByteOrder': {
        'values': [
            {
                'name': 'NIFGEN_VAL_LITTLE_ENDIAN',
                'value': 0,
            },
            {
                'name': 'NIFGEN_VAL_BIG_ENDIAN',
                'value': 1,
            },
        ],
    },
    'Signal': {
        'values': [
            {
                'name': 'NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK',
                'value': 1019,
            },
            {
                'name': 'NIFGEN_VAL_SYNC_OUT',
                'value': 1002,
            },
            {
                'name': 'NIFGEN_VAL_START_TRIGGER',
                'value': 1004,
            },
            {
                'name': 'NIFGEN_VAL_MARKER_EVENT',
                'value': 1001,
            },
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_TIMEBASE',
                'value': 1006,
            },
            {
                'name': 'NIFGEN_VAL_SYNCHRONIZATION',
                'value': 1007,
            },
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK',
                'value': 101,
            },
            {
                'name': 'NIFGEN_VAL_REFERENCE_CLOCK',
                'value': 102,
            },
            {
                'name': 'NIFGEN_VAL_SCRIPT_TRIGGER',
                'value': 103,
            },
            {
                'name': 'NIFGEN_VAL_READY_FOR_START_EVENT',
                'value': 105,
            },
            {
                'name': 'NIFGEN_VAL_STARTED_EVENT',
                'value': 106,
            },
            {
                'name': 'NIFGEN_VAL_DONE_EVENT',
                'value': 107,
            },
            {
                'name': 'NIFGEN_VAL_DATA_MARKER_EVENT',
                'value': 108,
            },
        ],
    },
    'HardwareState': {
        'values': [
            {
                'name': 'NIFGEN_VAL_IDLE',
                'value': 0,
            },
            {
                'name': 'NIFGEN_VAL_WAITING_FOR_START_TRIGGER',
                'value': 100,
            },
            {
                'name': 'NIFGEN_VAL_RUNNING',
                'value': 200,
            },
            {
                'name': 'NIFGEN_VAL_DONE',
                'value': 600,
            },
            {
                'name': 'NIFGEN_VAL_HARDWARE_ERROR',
                'value': 1000,
            },
        ],
    },
}

# TODO(bhaswath): Move this enum together with other enums once Issue #624 is fixed.
replacement_enums = {
    'Trigger': {
        'values': [
            {
                'name': 'NIFGEN_VAL_START_TRIGGER',
                'value': 1004,
            },
            {
                'name': 'NIFGEN_VAL_SCRIPT_TRIGGER',
                'value': 103,
            },
        ],
    },
}
