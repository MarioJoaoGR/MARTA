
import pytest
from dataclasses import dataclass
from dataclasses_json.mm import make_instance

@pytest.fixture
def person_class():
    @dataclass
    class Person:
        name: str
        age: int
    return Person

def test_make_instance(person_class):
    kvs = {'name': 'John'}
    kwargs = {'age': 30}
    person_instance = make_instance(person_class, kvs=kvs, **kwargs)
    
    assert isinstance(person_instance, person_class)
    assert person_instance.name == 'John'
    assert person_instance.age == 30

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_make_instance_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_make_instance_0_test_edge_cases.py:4:0: E0611: No name 'make_instance' in module 'dataclasses_json.mm' (no-name-in-module)

"""