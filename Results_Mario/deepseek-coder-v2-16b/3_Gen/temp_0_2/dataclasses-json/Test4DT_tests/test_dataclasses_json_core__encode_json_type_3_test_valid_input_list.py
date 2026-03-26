
import pytest
from dataclasses_json.core import _encode_json_type  # Assuming this is the correct module path

def test_valid_input_list():
    # Test a valid list input
    result = _encode_json_type([1, 2, {"key": "value"}])
    assert result == [1, 2, {'key': 'value'}]
    
    # Test nested lists and dictionaries
    result = _encode_json_type({"outer": {"inner": "value"}})
    assert result == {'outer': {'inner': 'value'}}
    
    # Test a non-list, non-dict input
    result = _encode_json_type("not a list or dict")
    assert result == "not a list or dict"
