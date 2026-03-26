
import pytest
from dataclasses_json import core as json_core

def test_valid_input_list():
    # Test with a valid list input
    result = json_core._encode_json_type([1, 2, {"key": "value"}])
    assert isinstance(result, list)
    assert result == [1, 2, {'key': 'value'}]
    
    # Test with a nested dictionary input
    result = json_core._encode_json_type({"outer": {"inner": "value"}})
    assert isinstance(result, dict)
    assert result == {'outer': {'inner': 'value'}}
    
    # Test with a non-list, non-dict input
    result = json_core._encode_json_type("not a list or dict")
    assert result == "not a list or dict"
