
import pytest
from your_module import _get_decoder_in_global_config  # Replace 'your_module' with the actual module name where the function is defined.

def test_invalid_input():
    with pytest.raises(KeyError):
        _get_decoder_in_global_config('nonexistent_type')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__get_decoder_in_global_config_1_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_1_test_invalid_input.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""