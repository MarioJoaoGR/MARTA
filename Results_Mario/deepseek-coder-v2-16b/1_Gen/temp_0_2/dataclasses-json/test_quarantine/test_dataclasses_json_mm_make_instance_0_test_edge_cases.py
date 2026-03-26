
import pytest
from dataclasses import dataclass
from dataclasses_json.mm import make_instance  # Assuming this is the correct module path

@dataclass
class Person:
    name: str
    age: int

def test_make_instance():
    person_instance = make_instance(Person, kvs={'name': 'Alice'}, **{'age': 30})
    assert person_instance.name == 'Alice'
    assert person_instance.age == 30

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_make_instance_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_make_instance_0_test_edge_cases.py:4:0: E0611: No name 'make_instance' in module 'dataclasses_json.mm' (no-name-in-module)


"""