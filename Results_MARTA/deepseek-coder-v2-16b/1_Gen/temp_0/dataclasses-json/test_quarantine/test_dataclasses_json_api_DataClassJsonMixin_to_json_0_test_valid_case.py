
import json
from dataclasses import dataclass
from your_module import DataClassJsonMixin, MyDataClass
import pytest

@dataclass
class MyDataClass(DataClassJsonMixin):
    name: str
    age: int

def test_valid_case():
    data = MyDataClass(name="John Doe", age=30)
    json_string = data.to_json()
    
    expected_output = '{"name": "John Doe", "age": 30}'
    assert json_string == expected_output, f"Expected {expected_output}, but got {json_string}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_DataClassJsonMixin_to_json_0_test_valid_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_to_json_0_test_valid_case.py:4:0: E0401: Unable to import 'your_module' (import-error)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_to_json_0_test_valid_case.py:8:0: E0102: class already defined line 4 (function-redefined)

"""