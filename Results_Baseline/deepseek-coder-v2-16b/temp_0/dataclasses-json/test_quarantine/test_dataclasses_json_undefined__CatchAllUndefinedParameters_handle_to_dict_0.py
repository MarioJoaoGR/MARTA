
# Module: dataclasses_json.undefined
import pytest
from dataclasses import dataclass
from dataclasses_json import dataclass_json, UndefinedParameterAction as _UndefinedParameterAction
from typing import Dict, Any

# Define a dataclass for testing
@dataclass_json
@dataclass
class Person:
    name: str
    age: int = 0

# Test data
valid_person_dict = {"name": "John Doe", "age": 30, "extra_param": "extra"}
invalid_person_dict = {"name": "Jane Doe"}

def test_handle_to_dict_with_undefined():
    # Create a Person instance from the dictionary with additional parameters
    person_instance = Person(**valid_person_dict)
    
    # Convert to dict, should include extra_param in the resulting dictionary
    result = _UndefinedParameterAction.handle_to_dict(person_instance, valid_person_dict)
    
    assert "extra_param" in result, "Expected 'extra_param' to be included in the dictionary."
    assert result["extra_param"] == "extra", "Unexpected value for 'extra_param'."

def test_handle_to_dict_without_undefined():
    # Create a Person instance from the dictionary without additional parameters
    person_instance = Person(**invalid_person_dict)
    
    # Convert to dict, should not include extra_param in the resulting dictionary
    result = _UndefinedParameterAction.handle_to_dict(person_instance, invalid_person_dict)
    
    assert "extra_param" not in result, "Unexpected 'extra_param' found in the dictionary."

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0.py:5:0: E0611: No name 'UndefinedParameterAction' in module 'dataclasses_json' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0.py:21:22: E1123: Unexpected keyword argument 'extra_param' in constructor call (unexpected-keyword-arg)

"""