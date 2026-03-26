
from dataclasses import dataclass
from typing import Optional, Union
from enum import Enum
from pytest import mark
from dataclasses_json import dataclass_json
from dataclasses_json.api import Undefined

class LetterCase(Enum):
    LOWER = "lower"
    UPPER = "upper"

@dataclass_json
@dataclass
class MyDataClass:
    name: str
    age: int
    email: Optional[str] = None

def test_edge_cases():
    my_instance = MyDataClass(name="John Doe", age=30, email="john.doe@example.com")
    json_string = my_instance.to_json(letter_case=LetterCase.LOWER, undefined=Undefined.EXCLUDE)
    assert json_string == '{"name": "John Doe", "age": 30}'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_dataclass_json_1_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_1_test_edge_cases.py:22:18: E1101: Instance of 'MyDataClass' has no 'to_json' member (no-member)


"""