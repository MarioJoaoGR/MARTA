
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

    # Test a non-list, non-dict input
    non_list_non_dict = "not a list or dict"
    encoded_non_list_non_dict = dcj_core._encode_json_type(non_list_non_dict)
    assert encoded_non_list_non_dict == "not a list or dict"
