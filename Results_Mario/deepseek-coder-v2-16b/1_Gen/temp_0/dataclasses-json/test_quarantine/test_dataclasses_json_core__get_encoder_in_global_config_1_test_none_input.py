
import pytest
from unittest.mock import patch
import cfg

@pytest.mark.parametrize("type_, expected", [
    (None, TypeError),  # Test with None as input
])
def test_none_input(type_, expected):
    with pytest.raises(expected):
        _get_encoder_in_global_config(type_)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__get_encoder_in_global_config_1_test_none_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_1_test_none_input.py:4:0: E0401: Unable to import 'cfg' (import-error)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_1_test_none_input.py:11:8: E0602: Undefined variable '_get_encoder_in_global_config' (undefined-variable)

"""