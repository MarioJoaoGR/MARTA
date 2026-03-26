
import pytest
from dataclasses import dataclass, fields
from typing import Union, Optional
from dataclasses_json.mm import IntSerializer, StrSerializer

@dataclass
class MyClass:
    my_field: Union[int, str]

def test_serialize():
    field = fields(MyClass)['my_field']
    assert isinstance(field, _UnionField)
    
    # Test with int value
    obj = MyClass(my_field=123)
    serialized = field._serialize(obj.my_field, 'my_field', obj)
    assert serialized == {'__type': 'int', 'value': 123}
    
    # Test with str value
    obj = MyClass(my_field="test")
    serialized = field._serialize(obj.my_field, 'my_field', obj)
    assert serialized == {'__type': 'str', 'value': 'test'}
    
    # Test with None value (allow_none should be True)
    obj = MyClass(my_field=None)
    serialized = field._serialize(obj.my_field, 'my_field', obj)
    assert serialized is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__UnionField__serialize_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_edge_cases.py:5:0: E0611: No name 'IntSerializer' in module 'dataclasses_json.mm' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_edge_cases.py:5:0: E0611: No name 'StrSerializer' in module 'dataclasses_json.mm' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_edge_cases.py:12:12: E1126: Sequence index is not an int, slice, or instance with __index__ (invalid-sequence-index)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_edge_cases.py:13:29: E0602: Undefined variable '_UnionField' (undefined-variable)


"""