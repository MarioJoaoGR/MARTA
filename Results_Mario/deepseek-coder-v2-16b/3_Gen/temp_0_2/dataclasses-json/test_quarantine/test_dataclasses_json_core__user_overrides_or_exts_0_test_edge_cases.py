
from dataclasses import fields
from collections import defaultdict
from dataclasses_json.core import FieldOverride

def _user_overrides_or_exts(cls):
    """
    Analyzes the user-defined overrides or extensions for fields in a dataclass and returns them as a dictionary of FieldOverride objects.

    This function inspects the global configuration settings, class-level metadata, and field-level metadata to determine any user-defined overrides or extensions for encoders, decoders, and mm_fields. It then constructs a dictionary where each key is a field name and the value is a FieldOverride object containing the appropriate configurations.

    Parameters:
        cls (type): The dataclass class to analyze for user-defined overrides or extensions.

    Returns:
        dict: A dictionary where keys are field names and values are FieldOverride objects, each containing the encoder, decoder, and mm_field configurations as specified by user overrides or extensions.

    Example:
        Suppose you have a dataclass `MyDataClass` with fields `name`, `age`, and `address`. The function will inspect these fields for any user-defined overrides or extensions in their metadata. If the field 'name' has an encoder specified, it will be included in the returned dictionary under the key 'name'.
    """
    global_metadata = defaultdict(dict)
    encoders = getattr(cfg.global_config, 'encoders', {})
    decoders = getattr(cfg.global_config, 'decoders', {})
    mm_fields = getattr(cfg.global_config, 'mm_fields', {})
    
    for field in fields(cls):
        if field.type in encoders:
            global_metadata[field.name]['encoder'] = encoders[field.type]
        if field.type in decoders:
            global_metadata[field.name]['decoder'] = decoders[field.type]
        if field.type in mm_fields:
            global_metadata[field.name]['mm_field'] = mm_fields[field.type]
    
    try:
        cls_config = getattr(cls, 'dataclass_json_config', {})
    except AttributeError:
        cls_config = {}

    overrides = {}
    for field in fields(cls):
        field_config = {}
        # first apply global overrides or extensions
        field_metadata = global_metadata[field.name]
        if 'encoder' in field_metadata:
            field_config['encoder'] = field_metadata['encoder']
        if 'decoder' in field_metadata:
            field_config['decoder'] = field_metadata['decoder']
        if 'mm_field' in field_metadata:
            field_config['mm_field'] = field_metadata['mm_field']
        # then apply class-level overrides or extensions
        field_config.update(cls_config)
        # last apply field-level overrides or extensions
        field_config.update(field.metadata.get('dataclasses_json', {}))
        overrides[field.name] = FieldOverride(**field_config)
    return overrides

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__user_overrides_or_exts_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__user_overrides_or_exts_0_test_edge_cases.py:22:23: E0602: Undefined variable 'cfg' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__user_overrides_or_exts_0_test_edge_cases.py:23:23: E0602: Undefined variable 'cfg' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__user_overrides_or_exts_0_test_edge_cases.py:24:24: E0602: Undefined variable 'cfg' (undefined-variable)


"""