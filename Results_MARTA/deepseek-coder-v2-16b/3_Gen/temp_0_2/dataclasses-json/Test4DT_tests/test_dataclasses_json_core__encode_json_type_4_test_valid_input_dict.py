
import pytest
from dataclasses_json.core import _encode_json_type, _ExtendedEncoder
from typing import Union, List, Dict

def test_valid_input_dict():
    # Test a valid dictionary input
    result = _encode_json_type({"outer": {"inner": "value"}})
    assert isinstance(result, dict)
    assert result == {'outer': {'inner': 'value'}}
    
    # Test a valid list input
    result_list = _encode_json_type([1, 2, {"key": "value"}])
    assert isinstance(result_list, list)
    assert result_list == [1, 2, {'key': 'value'}]
    
    # Test a non-JSON type input
    not_json = _encode_json_type("not a list or dict")
    assert not_json == "not a list or dict"
