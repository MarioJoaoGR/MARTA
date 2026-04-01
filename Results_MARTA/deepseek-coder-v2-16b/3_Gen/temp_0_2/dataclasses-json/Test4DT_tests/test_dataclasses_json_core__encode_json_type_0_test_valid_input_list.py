
import pytest
from dataclasses_json import core as dcj_core

def test_valid_input_list():
    # Test a valid list input
    result = dcj_core._encode_json_type([1, 2, {"key": "value"}])
    assert result == [1, 2, {'key': 'value'}]
    
    # Test a valid nested dictionary input
    result = dcj_core._encode_json_type({"outer": {"inner": "value"}})
    assert result == {'outer': {'inner': 'value'}}
    
    # Test an invalid non-list, non-dict input
    result = dcj_core._encode_json_type("not a list or dict")
    assert result == "not a list or dict"
