
import pytest
from dataclasses import dataclass
from your_module_path import make_instance  # Replace 'your_module_path' with the correct module path

@dataclass
class Person:
    name: str
    age: int

def test_valid_inputs():
    person_instance = make_instance(Person, kvs={'name': 'John'}, **{'age': 30})
    assert person_instance.name == 'John'
    assert person_instance.age == 30

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_make_instance_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_make_instance_0_test_valid_inputs.py:4:0: E0401: Unable to import 'your_module_path' (import-error)


"""