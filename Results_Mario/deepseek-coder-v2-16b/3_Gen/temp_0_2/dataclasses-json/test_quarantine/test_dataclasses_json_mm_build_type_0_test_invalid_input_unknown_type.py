
import pytest
from dataclasses_json.mm import build_type, fields
from marshmallow import warnings
from typing import Optional, Union, List, Tuple
from enum import Enum

class UnknownTypeClass:
    pass

@pytest.mark.parametrize("type_, options, expected_warning", [
    (UnknownTypeClass, {}, True),  # Test with an unknown type
])
def test_invalid_input_unknown_type(type_, options, expected_warning):
    with pytest.warns(UserWarning) if expected_warning else pytest.raises(AttributeError):
        result = build_type(UnknownTypeClass, options, None, None, UnknownTypeClass)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_invalid_input_unknown_type.py F [100%]

=================================== FAILURES ===================================
_______ test_invalid_input_unknown_type[UnknownTypeClass-options0-True] ________

type_ = <class 'Test4DT_tests.test_dataclasses_json_mm_build_type_0_test_invalid_input_unknown_type.UnknownTypeClass'>
options = {}, expected_warning = True

    @pytest.mark.parametrize("type_, options, expected_warning", [
        (UnknownTypeClass, {}, True),  # Test with an unknown type
    ])
    def test_invalid_input_unknown_type(type_, options, expected_warning):
        with pytest.warns(UserWarning) if expected_warning else pytest.raises(AttributeError):
>           result = build_type(UnknownTypeClass, options, None, None, UnknownTypeClass)

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_invalid_input_unknown_type.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/mm.py:293: in build_type
    return inner(type_, options)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

type_ = <class 'Test4DT_tests.test_dataclasses_json_mm_build_type_0_test_invalid_input_unknown_type.UnknownTypeClass'>
options = {}

    def inner(type_, options):
        while True:
            if not _is_new_type(type_):
                break
    
            type_ = type_.__supertype__
    
        if is_dataclass(type_):
            if _issubclass_safe(type_, mixin):
                options['field_many'] = bool(
                    _is_supported_generic(field.type) and _is_collection(
                        field.type))
                return fields.Nested(type_.schema(), **options)
            else:
                warnings.warn(f"Nested dataclass field {field.name} of type "
                              f"{field.type} detected in "
                              f"{cls.__name__} that is not an instance of "
                              f"dataclass_json. Did you mean to recursively "
                              f"serialize this field? If so, make sure to "
                              f"augment {type_} with either the "
                              f"`dataclass_json` decorator or mixin.")
                return fields.Field(**options)
    
        origin = getattr(type_, '__origin__', type_)
        args = [inner(a, {}) for a in getattr(type_, '__args__', []) if
                a is not type(None)]
    
        if type_ == Ellipsis:
            return type_
    
        if _is_optional(type_):
            options["allow_none"] = True
        if origin is tuple:
            if len(args) == 2 and args[1] == Ellipsis:
                return _TupleVarLen(args[0], **options)
            else:
                return fields.Tuple(args, **options)
        if origin in TYPES:
            return TYPES[origin](*args, **options)
    
        if _issubclass_safe(origin, Enum):
            return fields.Enum(enum=origin, by_value=True, *args, **options)
    
        if is_union_type(type_):
            union_types = [a for a in getattr(type_, '__args__', []) if
                           a is not type(None)]
            union_desc = dict(zip(union_types, args))
            return _UnionField(union_desc, cls, field, **options)
    
        warnings.warn(
>           f"Unknown type {type_} at {cls.__name__}.{field.name}: {field.type} "
            f"It's advised to pass the correct marshmallow type to `mm_field`.")
E       AttributeError: 'NoneType' object has no attribute 'name'

dataclasses-json/dataclasses_json/mm.py:289: AttributeError

During handling of the above exception, another exception occurred:

type_ = <class 'Test4DT_tests.test_dataclasses_json_mm_build_type_0_test_invalid_input_unknown_type.UnknownTypeClass'>
options = {}, expected_warning = True

    @pytest.mark.parametrize("type_, options, expected_warning", [
        (UnknownTypeClass, {}, True),  # Test with an unknown type
    ])
    def test_invalid_input_unknown_type(type_, options, expected_warning):
>       with pytest.warns(UserWarning) if expected_warning else pytest.raises(AttributeError):
E       Failed: DID NOT WARN. No warnings of type (<class 'UserWarning'>,) were emitted.
E        Emitted warnings: [].

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_invalid_input_unknown_type.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_invalid_input_unknown_type.py::test_invalid_input_unknown_type[UnknownTypeClass-options0-True]
============================== 1 failed in 0.04s ===============================
"""