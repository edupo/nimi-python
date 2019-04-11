# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning enums that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not codegen enums associated with P2P or External Calibration since neither 
# are supported in Python
enums_codegen_method = {
    'DigitsResolution': {'codegen_method': 'no', },  # Enum metadata actually contains constants. Also need to remove to generate valid code
    'PowerlineFrequency': {'codegen_method': 'no', }, # Enum metadata actually contains constants.
    'CurrentSource': {'codegen_method': 'no', }, # Enum metadata actually contains constants.
    'InputResistance': {'codegen_method': 'no', }, # Enum metadata actually contains constants.
    'DCBias': {'codegen_method': 'no', },  # Delete because boolean values only
    'OffsetCompensatedOhms': {'codegen_method': 'no', },  # Delete because boolean values only
}

enums_additional_enums = {
}

# Override names that can't be directly converted from C names into valid Python names
enums_override_values = {
    'Function': { 'values': {
        4: { 'python_name': 'TWO_WIRE_RES', },
        5: { 'python_name': 'FOUR_WIRE_RES', },
        8: { 'name': 'NIDMM_VAL_TEMPERATURE', },
    }, },
    'ThermistorType': { 'values': {
        1: { 'python_name': 'TEMP_THERMISTOR_THERMISTOR_44004', },
        2: { 'python_name': 'TEMP_THERMISTOR_THERMISTOR_44006', },
        3: { 'python_name': 'TEMP_THERMISTOR_THERMISTOR_44007', },
    }, },
    'TransducerType': { 'values': {
        2: { 'python_name': 'TWO_WIRE_RTD', },
        3: { 'python_name': 'FOUR_WIRE_RTD', },
    }, },
}

