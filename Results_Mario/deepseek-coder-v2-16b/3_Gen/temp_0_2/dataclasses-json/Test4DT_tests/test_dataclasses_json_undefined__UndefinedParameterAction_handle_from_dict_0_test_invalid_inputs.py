
import pytest
from dataclasses import dataclass
from dataclasses_json.undefined import _UndefinedParameterAction
from typing import Dict, Any

@dataclass
class Person:
    name: str
    age: int = 0

def test_handle_from_dict_invalid_inputs():
    # Test with a dictionary containing non-string keys
    invalid_input1 = {123: 'John Doe', 'age': 30}
    result1 = _UndefinedParameterAction.handle_from_dict(Person, invalid_input1)
    assert not result1, "Expected an empty dictionary for invalid input"

    # Test with a dictionary containing extra keys
    invalid_input2 = {'name': 'John Doe', 'age': 30, 'extra_key': 'value'}
    result2 = _UndefinedParameterAction.handle_from_dict(Person, invalid_input2)
    assert not result2, "Expected an empty dictionary for invalid input"

    # Test with a dictionary containing non-string keys but valid ones present
    invalid_input3 = {'name': 'John Doe', 123: 30}
    result3 = _UndefinedParameterAction.handle_from_dict(Person, invalid_input3)
    assert not result3, "Expected an empty dictionary for invalid input"
