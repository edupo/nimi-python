# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release

attributes_codegen_method = {
    1050401: { "codegen_method": "no"      },  # GROUP_CAPABILITIES - IVI Attribute - #824
    1050021: { "codegen_method": "no"      },  # INTERCHANGE_CHECK - IVI Attribute - #824
    1050002: { "codegen_method": "no"      },  # RANGE_CHECK - IVI Attribute - #824
    1050006: { "codegen_method": "no"      },  # RECORD_COERCIONS - IVI Attribute - #824
    1050515: { "codegen_method": "no"      },  # SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION - IVI Attribute - #824
    1050516: { "codegen_method": "no"      },  # SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION - IVI Attribute - #824
    1050004: { "codegen_method": "no"      },  # CACHE - IVI Attribute - #824
    1150074: { "codegen_method": "private" },  # ACTIVE_ADVANCED_SEQUENCE - Advanced Sequence Attribute - #793
    1150075: { "codegen_method": "private" },  # ACTIVE_ADVANCED_SEQUENCE_STEP - Advanced Sequence Attribute - #793
    1150035: { "codegen_method": "no"      },  # DIGITAL_EDGE_MEASURE_TRIGGER_EDGE - Backplane only, always falling edge - #860
    1150096: { "codegen_method": "no"      },  # DIGITAL_EDGE_PULSE_TRIGGER_EDGE - Backplane only, always falling edge - #860
    1150027: { "codegen_method": "no"      },  # DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE - Backplane only, always falling edge - #860
    1150031: { "codegen_method": "no"      },  # DIGITAL_EDGE_SOURCE_TRIGGER_EDGE - Backplane only, always falling edge - #860
    1150022: { "codegen_method": "no"      },  # DIGITAL_EDGE_START_TRIGGER_EDGE - Backplane only, always falling edge - #860
}

attributes_converters = {
    1150046: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # MEASURE_COMPLETE_EVENT_DELAY
    1150065: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # MEASURE_RECORD_DELTA_TIME
    1150093: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # PULSE_ON_TIME
    1150094: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # PULSE_OFF_TIME
    1150051: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # SOURCE_DELAY
}


