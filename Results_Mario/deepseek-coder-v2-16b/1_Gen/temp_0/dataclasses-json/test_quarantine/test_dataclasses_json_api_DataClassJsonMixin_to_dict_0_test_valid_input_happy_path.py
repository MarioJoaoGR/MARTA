
import pytest
from your_module import MyDataClass, DataClassJsonMixin
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class MyDataClass(DataClassJsonMixin):
    name: str
    age: int

def test_valid_input_happy_path():
    data = MyDataClass(name='John Doe', age=30)
    result = data.to_dict()
    assert isinstance(result, dict), "Expected a dictionary"
    assert 'name' in result and result['name'] == 'John Doe', "Name field is incorrect"
    assert 'age' in result and result['age'] == 30, "Age field is incorrect"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_DataClassJsonMixin_to_dict_0_test_valid_input_happy_path
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_to_dict_0_test_valid_input_happy_path.py:3:0: E0401: Unable to import 'your_module' (import-error)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_to_dict_0_test_valid_input_happy_path.py:8:0: E0102: class already defined line 3 (function-redefined)

"""