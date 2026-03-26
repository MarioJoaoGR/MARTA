
import pytest
from dataclasses_json import core as dcj_core

def test_valid_input_dict():
    # Test a valid dictionary input
    value = {"key": "value"}
    encoded = dcj_core._encode_json_type(value)
    assert encoded == {"key": "value"}

    # Test nested dictionaries
    nested_value = {"outer": {"inner": "value"}}
    encoded_nested = dcj_core._encode_json_type(nested_value)
    assert encoded_nested == {"outer": {"inner": "value"}}

    # Test a non-dict, non-list input
    non_dict_non_list = "not a list or dict"
    encoded_non_dict_non_list = dcj_core._encode_json_type(non_dict_non_list)
    assert encoded_non_dict_non_list == "not a list or dict"
