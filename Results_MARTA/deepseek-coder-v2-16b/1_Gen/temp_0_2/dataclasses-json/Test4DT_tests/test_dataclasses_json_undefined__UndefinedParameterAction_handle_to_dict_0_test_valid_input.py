
import pytest
from dataclasses_json import undefined
from typing import Any, Dict

def handle_to_dict(obj, kvs: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Return the parameters that will be written to the output dict
    """
    return kvs

def test_valid_input():
    # Test with a valid dictionary input
    input_dict = {'key1': 'value1', 'key2': 'value2'}
    result = handle_to_dict(None, input_dict)
    assert result == input_dict
