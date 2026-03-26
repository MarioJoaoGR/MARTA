
import warnings
from dataclasses import is_dataclass
from typing import Union, get_origin as _get_type_origin
from dataclasses_json.mm import _issubclass_safe

class _UnionField:
    """
    A class representing a union field within a data structure.

    This class is designed to encapsulate the description, class type, and specific field of a union in a more complex data model.

    Parameters:
        desc (dict): A dictionary where keys are possible types and values are schema objects that can handle those types. This dict should map directly to the schemas defined in `desc` of the calling context.
        cls (type): The class associated with this union field, which is necessary for serialization but not used during instantiation.
        field: The specific field within the class that this union represents, also used only for informational purposes and not instantiated by this class.
        allow_none (bool): A flag indicating whether to allow `None` values in the serialized output. If True, `None` will be returned as is; if False, it will attempt to serialize any non-None value.

    Returns:
        dict or None: The serialized representation of the value according to its type, or None if the value is allowed to be None and matches this condition.

    Example:
        >>> from dataclasses import dataclass
        >>> from typing import Union
        
        @dataclass
        class Person:
            name: str
            age: int
        
        schema = {Person: lambda v, a, o, **k: {'name': v.name, 'age': v.age}}
        
        union_field = _UnionField(desc=schema, cls=Person, field='person')
        person_instance = Person(name="John Doe", age=30)
        serialized_person = union_field._serialize(person_instance)
        print(serialized_person)  # Output: {'name': 'John Doe', 'age': 30, '__type': 'Person'}
        
        noneserialized_person = union_field._serialize(None)
        print(noneserialized_person)  # Output: None (assuming allow_none is True)
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
            if _issubclass_safe(type(value), type_):
                if is_dataclass(value):
                    res = schema_._serialize(value, attr, obj, **kwargs)
                    res['__type'] = str(type_.__name__)
                    return res
                break
            elif isinstance(value, _get_type_origin(type_)):
                return schema_._serialize(value, attr, obj, **kwargs)
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
************* Module Test4DT_tests.test_dataclasses_json_mm__UnionField__serialize_0_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_edge_case.py:65:15: E1101: Super of '_UnionField' has no '_serialize' member (no-member)


"""