
import warnings
from dataclasses import is_dataclass
from typing import Union, get_origin as _get_type_origin

class _UnionField:
    """
    A class representing a union field within a data structure.

    This class is designed to encapsulate the description, class type, and specific field of a union in a more complex data model.

    Parameters:
        desc (dict): A dictionary where keys are possible types and values are schema objects that can handle those types. This dict should map directly to the schemas defined in `desc` of the calling context.
        cls (type): The class associated with this union field, which is necessary for serialization but not used during instantiation.
        field: The specific field within the class that this union represents, also used only for informational purposes and not instantiated by this class.
        allow_none (bool): A flag indicating whether to allow `None` values in the serialized output. If True, `None` will be returned as is; if False, it will attempt to serialize any non-None value.
    """
    def __init__(self, desc, cls, field, allow_none=False):
        self.desc = desc
        self.cls = cls
        self.field = field
        self.allow_none = allow_none

    def _serialize(self, value, attr, obj, **kwargs):
        if self.allow_none and value is None:
            return None
        for type_, schema_ in self.desc.items():
            if isinstance(value, type_) or (type_ is Union and any(_issubclass_safe(value, t) for t in type_.__args__)):
                if is_dataclass(value):
                    res = schema_._serialize(value, attr, obj, **kwargs)
                    res['__type'] = str(type_.__name__)
                    return res
                else:
                    return schema_._serialize(value, attr, obj, **kwargs)
        warnings.warn(
            f'The type "{type(value).__name__}" (value: "{value}") '
            f'is not in the list of possible types of typing.Union '
            f'(dataclass: {self.cls.__name__}, field: {self.field}). '
            f'Value cannot be serialized properly.'
        )
        return super()._serialize(value, attr, obj, **kwargs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__UnionField__serialize_0_test_none_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_none_input.py:28:67: E0602: Undefined variable '_issubclass_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_none_input.py:41:15: E1101: Super of '_UnionField' has no '_serialize' member (no-member)


"""