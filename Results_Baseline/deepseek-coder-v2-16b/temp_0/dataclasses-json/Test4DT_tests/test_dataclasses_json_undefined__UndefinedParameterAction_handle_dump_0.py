# Module: dataclasses_json.undefined
import pytest
from dataclasses import dataclass
from typing import Any, Dict
from dataclasses_json.undefined import _UndefinedParameterAction as DataProcessor

# Test cases for handle_dump function

@dataclass
class ConfigClass:
    param1: int = 10
    param2: str = "example"

class CustomObject:
    def __init__(self, param1: int, param2: str):
        self.param1 = param1
        self.param2 = param2

config_dict = {"param1": 30, "param2": "sample"}

# Test case for handling a dataclass instance
def test_handle_dump_dataclass():
    config_instance = ConfigClass()
    result = DataProcessor.handle_dump(config_instance)
    assert isinstance(result, dict), f"Expected a dictionary but got {type(result)}"
    assert len(result) == 0, "Expected an empty dictionary for dataclass instance"

# Test case for handling a custom object
def test_handle_dump_custom_object():
    custom_obj = CustomObject(param1=20, param2="test")
    result = DataProcessor.handle_dump(custom_obj)
    assert isinstance(result, dict), f"Expected a dictionary but got {type(result)}"
    assert len(result) == 0, "Expected an empty dictionary for custom object"

# Test case for handling a dictionary
def test_handle_dump_dictionary():
    result = DataProcessor.handle_dump(config_dict)
    assert isinstance(result, dict), f"Expected a dictionary but got {type(result)}"
    assert len(result) == 0, "Expected an empty dictionary for dictionary input"

# Test case to ensure the function returns an empty dictionary by default
def test_handle_dump_default():
    result = DataProcessor.handle_dump(None)
    assert isinstance(result, dict), f"Expected a dictionary but got {type(result)}"
    assert len(result) == 0, "Expected an empty dictionary for None input"
