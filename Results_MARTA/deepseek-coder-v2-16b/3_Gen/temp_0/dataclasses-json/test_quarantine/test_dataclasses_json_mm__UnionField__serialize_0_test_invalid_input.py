
import pytest
from dataclasses import dataclass, fields
from typing import Union, Optional
from dataclasses_json.mm import _UnionField, is_dataclass, _issubclass_safe, _get_type_origin
from marshmallow import Schema, fields as mfields
import warnings

# Define serializers for the union field types
class IntSerializer(Schema):
    class Meta:
        fields = ('value',)

class StrSerializer(Schema):
    class Meta:
        fields = ('text',)

def test_invalid_input():
    @dataclass
    class MyClass:
        my_field: Union[int, str] = None

    # Define a union field with possible types and serializers
    desc = {int: IntSerializer, str: StrSerializer}
    my_union_field = _UnionField(desc, MyClass, "my_field")

    # Test invalid input type (None)
    value = None
    result = my_union_field._serialize(value, 'my_field', MyClass())

    assert result is None, f"Expected None but got {result}"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        @dataclass
        class MyClass:
            my_field: Union[int, str] = None
    
        # Define a union field with possible types and serializers
        desc = {int: IntSerializer, str: StrSerializer}
        my_union_field = _UnionField(desc, MyClass, "my_field")
    
        # Test invalid input type (None)
        value = None
>       result = my_union_field._serialize(value, 'my_field', MyClass())

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_invalid_input.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <fields._UnionField(dump_default=<marshmallow.missing>, attribute=None, validate=None, required=False, load_only=False...equired': 'Missing data for required field.', 'null': 'Field may not be null.', 'validator_failed': 'Invalid value.'})>
value = None, attr = 'my_field'
obj = test_invalid_input.<locals>.MyClass(my_field=None), kwargs = {}
type_ = <class 'str'>
schema_ = <class 'Test4DT_tests.test_dataclasses_json_mm__UnionField__serialize_0_test_invalid_input.StrSerializer'>

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
>               f'(dataclass: {self.cls.__name__}, field: {self.field.name}). '
                f'Value cannot be serialized properly.')
E           AttributeError: 'str' object has no attribute 'name'

dataclasses-json/dataclasses_json/mm.py:91: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.05s ===============================
"""