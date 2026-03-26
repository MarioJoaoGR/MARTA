
import pytest
from dataclasses import dataclass
from typing import Union
from dataclasses_json.mm import _UnionField

@dataclass
class Person:
    name: str
    age: int

schema = {Person: lambda v, a, o, **k: {'name': v.name, 'age': v.age}}

union_field = _UnionField(desc=schema, cls=Person, field='person')

def test_valid_inputs():
    person_instance = Person(name="John Doe", age=30)
    serialized_person = union_field._serialize(person_instance)
    assert serialized_person == {'name': 'John Doe', 'age': 30, '__type': 'Person'}
    
    noneserialized_person = union_field._serialize(None)
    assert noneserialized_person is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__UnionField__serialize_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_valid_inputs.py:18:24: E1120: No value for argument 'attr' in method call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_valid_inputs.py:18:24: E1120: No value for argument 'obj' in method call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_valid_inputs.py:21:28: E1120: No value for argument 'attr' in method call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_valid_inputs.py:21:28: E1120: No value for argument 'obj' in method call (no-value-for-parameter)


"""