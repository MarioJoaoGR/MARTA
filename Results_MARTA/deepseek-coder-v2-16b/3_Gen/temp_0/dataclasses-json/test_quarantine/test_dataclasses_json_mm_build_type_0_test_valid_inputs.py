
import warnings
from dataclasses import is_dataclass
from inspect import Parameter as FieldInfo
from typing import get_origin, get_args, Union, Tuple, Optional, Any, Enum
from marshmallow import fields
from marshmallow.fields import Field
from dataclasses_json.mm import _UnionField  # Corrected import path

# Assuming TYPES is a dictionary mapping type origins to their respective Marshmallow field classes
TYPES = {
    list: fields.List,
    tuple: fields.Tuple,
    Optional: fields.Nested,
    Union: fields.Raw,  # Adjust this based on actual usage of Union in your code
}

def build_type(type_, options, mixin, field: FieldInfo, cls):
    def inner(type_, options):
        while True:
            if not _is_new_type(type_):
                break
            type_ = type_.__supertype__

        if is_dataclass(type_):
            if _issubclass_safe(type_, mixin):
                options['field_many'] = bool(_is_supported_generic(field.type) and _is_collection(field.type))
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

        origin = get_origin(type_)
        args = [inner(a, {}) for a in get_args(type_) if a is not type(None)]

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
            union_types = [a for a in get_args(type_) if a is not type(None)]
            union_desc = dict(zip(union_types, args))
            return _UnionField(union_desc, cls, field, **options)

        warnings.warn(f"Unknown type {type_} at {cls.__name__}.{field.name}: {field.type} "
                      f"It's advised to pass the correct marshmallow type to `mm_field`.")
        return fields.Field(**options)

    return inner(type_, options)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_build_type_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py:5:0: E0611: No name 'Enum' in module 'typing' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py:21:19: E0602: Undefined variable '_is_new_type' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py:26:15: E0602: Undefined variable '_issubclass_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py:27:45: E0602: Undefined variable '_is_supported_generic' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py:27:83: E0602: Undefined variable '_is_collection' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py:45:11: E0602: Undefined variable '_is_optional' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py:49:23: E0602: Undefined variable '_TupleVarLen' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py:55:11: E0602: Undefined variable '_issubclass_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py:58:11: E0602: Undefined variable 'is_union_type' (undefined-variable)


"""