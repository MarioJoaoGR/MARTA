
import pytest
from your_module import _has_encoder_in_global_config  # Replace `your_module` with the actual module name where `_has_encoder_in_global_config` is defined
from dataclasses_json.core import cfg  # Assuming this is the correct import path for cfg in your setup

# Mocking the global configuration and its encoders
class MockConfig:
    def __init__(self):
        self.encoders = {}

cfg.global_config = MockConfig()

def test_invalid_input():
    # Test with None input
    assert not _has_encoder_in_global_config(None)
    
    # Test with non-string type
    with pytest.raises(TypeError):  # Assuming the function raises TypeError for invalid types
        _has_encoder_in_global_config(123)  # Example of an invalid input (integer)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_encoder_in_global_config_0_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_invalid_input.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""