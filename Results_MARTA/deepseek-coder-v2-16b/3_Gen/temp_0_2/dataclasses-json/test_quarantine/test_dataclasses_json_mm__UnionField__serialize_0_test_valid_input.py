
import warnings
from dataclasses import is_dataclass
from typing import Union
from dataclasses_json.mm import _get_type_origin

class _UnionField:
    def __init__(self, desc, cls, field, *args, **kwargs):
        self.desc = desc
        self.cls = cls
        self.field = field
        super().__init__(*args, **kwargs)

    def _serialize(self, value, attr, obj, **kwargs):
        if self.allow_none and value is None:
            return None
        for type_, schema_ in self.desc.items():
            if isinstance(value, type_) or (hasattr(type_, '__origin__') and isinstance(value, type_.__origin__)):
                if is_dataclass(value):
                    res = schema_._serialize(value, attr, obj, **kwargs)
                    res['__type'] = str(type_.__name__)
                    return res
                break
        else:
            warnings.warn(
                f'The type "{type(value).__name__}" (value: "{value}") '
                f'is not in the list of possible types of typing.Union '
                f'(dataclass: {self.cls.__name__}, field: {self.field.name}). '
                f'Value cannot be serialized properly.')
        return super()._serialize(value, attr, obj, **kwargs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__UnionField__serialize_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_valid_input.py:15:11: E1101: Instance of '_UnionField' has no 'allow_none' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_valid_input.py:30:15: E1101: Super of '_UnionField' has no '_serialize' member (no-member)


"""