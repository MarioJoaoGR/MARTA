
from dataclasses import fields, get_type_hints, is_dataclass
from typing import Type, Optional
import warnings
from dataclasses_json.core import (
    _isinstance_safe, _user_overrides_or_exts, _decode_letter_case_overrides,
    _handle_undefined_parameters_safe, _is_optional, _is_new_type,
    _is_supported_generic, _decode_generic, _support_extended_types
)
from dataclasses import dataclass

def _decode_dataclass(cls: Type[A], kvs: dict, infer_missing: bool) -> A:
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
                    warnings.warn(
                        f"Missing {warning} and was defaulted to None by "
                        f"infer_missing=True. "
                        f"Set infer_missing=False (the default) to prevent "
                        f"this behavior.", RuntimeWarning
                    )
                else:
                    warnings.warn(
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
            if field_type is type(field_value):
                init_kwargs[field.name] = field_value
            else:
                init_kwargs[field.name] = overrides[field.name].decoder(field_value)
        elif is_dataclass(field_type):
            value = _decode_dataclass(field_type, field_value, infer_missing)
            init_kwargs[field.name] = value
        elif _is_supported_generic(field_type) and field_type != str:
            init_kwargs[field.name] = _decode_generic(field_type, field_value, infer_missing)
        else:
            init_kwargs[field.name] = _support_extended_types(field_type, field_value)

    return cls(**init_kwargs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__decode_dataclass_0_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_0_test_edge_case.py:2:0: E0611: No name 'get_type_hints' in module 'dataclasses' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_0_test_edge_case.py:12:32: E0602: Undefined variable 'A' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_0_test_edge_case.py:12:71: E0602: Undefined variable 'A' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_0_test_edge_case.py:23:32: E0602: Undefined variable 'MISSING' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_0_test_edge_case.py:25:42: E0602: Undefined variable 'MISSING' (undefined-variable)

"""