
import pytest
from dataclasses_json.mm import make_instance

# Assuming 'Person' is defined somewhere in this module or imported
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def test_invalid_inputs():
    with pytest.raises(TypeError):  # We expect a TypeError because of incorrect parameters
        make_instance(Person, kvs={'name': 'John'}, **{'age': 30})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_make_instance_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_make_instance_0_test_invalid_inputs.py:3:0: E0611: No name 'make_instance' in module 'dataclasses_json.mm' (no-name-in-module)

"""