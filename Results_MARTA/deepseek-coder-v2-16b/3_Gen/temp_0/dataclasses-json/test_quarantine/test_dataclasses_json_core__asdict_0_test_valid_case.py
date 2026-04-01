
import pytest
from dataclasses_json.core import asdict  # Importing asdict from dataclasses_json.core

# Assuming MyDataClass is defined somewhere in your module
class MyDataClass:
    name: str
    age: int

def test_valid_case():
    data = MyDataClass(name="John Doe", age=30)
    result = asdict(data)
    assert isinstance(result, dict)
    assert result == {'name': 'John Doe', 'age': 30}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__asdict_0_test_valid_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_valid_case.py:3:0: E0611: No name 'asdict' in module 'dataclasses_json.core' (no-name-in-module)


"""