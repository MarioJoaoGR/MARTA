
import pytest
from dataclasses import dataclass
from typing import Dict, Optional
from dataclasses_json.api import DataClassJsonMixin

@dataclass
class TestDataClass(DataClassJsonMixin):
    name: str
    age: int

def test_invalid_input():
    with pytest.raises(TypeError):
        # Create an instance of a class that does not inherit from DataClassJsonMixin
        class InvalidType:
            pass
        
        invalid_instance = InvalidType()
        invalid_instance.to_dict()  # This should raise TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_DataClassJsonMixin_to_dict_1_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_to_dict_1_test_invalid_input.py:19:8: E1101: Instance of 'InvalidType' has no 'to_dict' member (no-member)


"""