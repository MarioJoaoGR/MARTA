
import pytest
from dataclasses_json import undefined
from typing import Dict, Any

class MyClass:
    def __init__(self):
        self.param1 = 'value1'
        self.param2 = 42

def handle_to_dict(obj, kvs: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Return the parameters that will be written to the output dict
    """
    return kvs

def test_valid_inputs():
    my_instance = MyClass()
    result = handle_to_dict(my_instance, {})
    assert result == {}
