
import json
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Type, Optional, Callable, Any
from unittest.mock import patch
import pytest
from dataclasses_json.api import DataClassJsonMixin

@dataclass
class Person:
    name: str
    age: int
    birth_date: datetime

def test_valid_input():
    json_str = '{"name": "Alice", "age": 30, "birth_date": "1992-05-20"}'
    
    with patch('dataclasses_json.api.DataClassJsonMixin.from_dict') as mock_from_dict:
        # Configure the mock to return a Person instance when called
        mock_instance = Person(name="Alice", age=30, birth_date=datetime(1992, 5, 20))
        mock_from_dict.return_value = mock_instance
        
        # Call the method under test
        result = DataClassJsonMixin.from_json(Person, json_str)
        
        # Assert that from_dict was called with the correct arguments
        mock_from_dict.assert_called_once_with({'name': 'Alice', 'age': 30, 'birth_date': datetime(1992, 5, 20)}, infer_missing=False)
        
        # Assert that the result is an instance of Person and has the correct values
        assert isinstance(result, Person)
        assert result.name == "Alice"
        assert result.age == 30
        assert result.birth_date == datetime(1992, 5, 20)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_DataClassJsonMixin_from_json_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_json_0_test_valid_input.py:26:17: E1121: Too many positional arguments for classmethod call (too-many-function-args)


"""