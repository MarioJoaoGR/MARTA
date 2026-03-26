
import pytest
from dataclasses import dataclass, fields
from typing import Optional, Union
from enum import Enum
from dataclasses_json.api import dataclass_json

class LetterCase(Enum):
    LOWER = "lower"
    UPPER = "upper"

@dataclass_json
@dataclass
class MyDataClass:
    name: str
    age: int
    email: Optional[str] = None

def test_valid_inputs():
    # Create an instance of MyDataClass
    my_instance = MyDataClass(name="John Doe", age=30, email="john.doe@example.com")
    
    # Convert to JSON string with specific letter case and undefined handling
    json_string = my_instance.to_json(letter_case=LetterCase.LOWER, undefined='exclude')
    
    # Check the output format
    assert json_string == '{"name": "John Doe", "age": 30}'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_dataclass_json_1_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_1_test_valid_inputs.py:24:18: E1101: Instance of 'MyDataClass' has no 'to_json' member (no-member)


"""