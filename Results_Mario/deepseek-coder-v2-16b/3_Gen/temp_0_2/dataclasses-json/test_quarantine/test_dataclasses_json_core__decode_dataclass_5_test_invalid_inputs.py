
import pytest
from dataclasses import is_dataclass, get_type_hints, fields
from typing import Type
from warnings import warn

def _decode_dataclass(cls, kvs, infer_missing):
    """
    Deserializes a JSON string into a dataclass instance. This function uses the `json` module to parse the JSON data and then converts it into a dictionary before passing it to the dataclass's `from_dict` method for instantiation. It supports optional parameters for custom parsing of float, int, and constant values, as well as an option to infer missing fields.

    Parameters:
        cls (Type[A]): The dataclass type to be instantiated from the JSON string.
        kvs (Json): A JSON-compatible data structure or a JSON formatted string representing the dictionary to be converted into a dataclass instance.
        infer_missing (bool): If True, missing fields will be inferred by comparing the dataclass and the dictionary schema. Default is False.

    Returns:
        A: An instance of the dataclass `cls` populated with data from the JSON string.
    """
    if _isinstance_safe(kvs, cls):
        return kvs
    overrides = _user_overrides_or_exts(cls)
    kvs = {} if kvs is None and infer_missing else kvs
    field_names = [field.name for field in fields(cls)]
    decode_names = _decode_letter_case_overrides(field_names, overrides)
    kvs = {decode_names.get(k, k): v for k, v in kvs.items()}
    missing_fields = {field for field in fields(cls) if field.name not in kvs}

    for field in missing_fields:
        if field.default is not MISSING:
            kvs[field.name] = field.default
        elif field.default_factory is not MISSING:
            kvs[field.name] = field.default_factory()
        elif infer_missing:
            kvs[field.name] = None

    # Perform undefined parameter action
    kvs = _handle_undefined_parameters_safe(cls, kvs, usage="from")

    init_kwargs = {}
    types = get_type_hints(cls)
    for field in fields(cls):
        # The field should be skipped from being added
        # to init_kwargs as it's not intended as a constructor argument.
        if not field.init:
            continue

        field_value = kvs[field.name]
        field_type = types[field.name]
        if field_value is None:
            if not _is_optional(field_type):
                warning = (
                    f"value of non-optional type {field.name} detected "
                    f"when decoding {cls.__name__}"
                )
                if infer_missing:
                    warn(
                        f"Missing {warning} and was defaulted to None by "
                        f"infer_missing=True. "
                        f"Set infer_missing=False (the default) to prevent "
                        f"this behavior.", RuntimeWarning
                    )
                else:
                    warn(
                        f"'NoneType' object {warning}.", RuntimeWarning
                    )
            init_kwargs[field.name] = field_value
            continue

        while True:
            if not _is_new_type(field_type):
                break

            field_type = field_type.__supertype__

        if (field.name in overrides
                and overrides[field.name].decoder is not None):
            # FIXME hack
            if field_type is type(field_value):
                init_kwargs[field.name] = field_value
            else:
                init_kwargs[field.name] = overrides[field.name].decoder(
                    field_value)
        elif is_dataclass(field_type):
            # FIXME this is a band-aid to deal with the value already being
            # serialized when handling nested marshmallow schema
            # proper fix is to investigate the marshmallow schema generation
            # code
            if is_dataclass(field_value):
                value = field_value
            else:
                value = _decode_dataclass(field_type, field_value,
                                          infer_missing)
            init_kwargs[field.name] = value
        elif _is_supported_generic(field_type) and field_type != str:
            init_kwargs[field.name] = _decode_generic(field_type,
                                                      field_value,
                                                      infer_missing)
        else:
            init_kwargs[field.name] = _support_extended_types(field_type,
                                                              field_value)

    return cls(**init_kwargs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__decode_dataclass_5_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_5_test_invalid_inputs.py:3:0: E0611: No name 'get_type_hints' in module 'dataclasses' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_5_test_invalid_inputs.py:19:7: E0602: Undefined variable '_isinstance_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_5_test_invalid_inputs.py:21:16: E0602: Undefined variable '_user_overrides_or_exts' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_5_test_invalid_inputs.py:24:19: E0602: Undefined variable '_decode_letter_case_overrides' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_5_test_invalid_inputs.py:29:32: E0602: Undefined variable 'MISSING' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_5_test_invalid_inputs.py:31:42: E0602: Undefined variable 'MISSING' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_5_test_invalid_inputs.py:37:10: E0602: Undefined variable '_handle_undefined_parameters_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_5_test_invalid_inputs.py:50:19: E0602: Undefined variable '_is_optional' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_5_test_invalid_inputs.py:70:19: E0602: Undefined variable '_is_new_type' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_5_test_invalid_inputs.py:94:13: E0602: Undefined variable '_is_supported_generic' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_5_test_invalid_inputs.py:95:38: E0602: Undefined variable '_decode_generic' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_5_test_invalid_inputs.py:99:38: E0602: Undefined variable '_support_extended_types' (undefined-variable)


"""