
import pytest
from dataclasses import dataclass
from dataclasses_json.mm import make_instance as mm_make_instance

@dataclass
class Person:
    name: str
    age: int

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # This should raise a TypeError because the function expects a dataclass instance, not a class
        mm_make_instance(Person, kvs={'name': 'John'}, **{'age': 30})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_make_instance_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_make_instance_0_test_invalid_inputs.py:4:0: E0611: No name 'make_instance' in module 'dataclasses_json.mm' (no-name-in-module)


"""