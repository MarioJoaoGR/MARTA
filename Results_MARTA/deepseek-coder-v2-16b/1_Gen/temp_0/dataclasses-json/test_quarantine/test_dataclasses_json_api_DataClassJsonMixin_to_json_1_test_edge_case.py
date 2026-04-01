
from dataclasses_json.api import DataClassJsonMixin
import pytest
import json
from typing import Optional, Union, Tuple, Callable
import dataclasses

@pytest.fixture
def data_class():
    @dataclasses.dataclass
    class MyDataClass(DataClassJsonMixin):
        name: str
        age: int
    return MyDataClass(name="John Doe", age=30)

def test_to_json(data_class):
    json_string = data_class.to_json()
    expected_output = json.dumps({"name": "John Doe", "age": 30}, cls=_ExtendedEncoder, sort_keys=False)
    assert json_string == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_DataClassJsonMixin_to_json_1_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_to_json_1_test_edge_case.py:18:70: E0602: Undefined variable '_ExtendedEncoder' (undefined-variable)

"""