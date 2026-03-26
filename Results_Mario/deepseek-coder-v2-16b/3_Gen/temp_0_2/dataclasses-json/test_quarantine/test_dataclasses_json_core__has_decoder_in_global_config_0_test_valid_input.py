
import pytest
from dataclasses_json.core import cfg  # Assuming this is the correct module path

# Mocking the global configuration object
class MockConfig:
    decoders = {"some_decoder_type": lambda x: None, "another_decoder_type": lambda x: None}

def test_valid_input():
    # Set up the mock config
    cfg.global_config = MockConfig()
    
    from dataclasses_json_core import _has_decoder_in_global_config  # Assuming this is the correct module path
    
    assert _has_decoder_in_global_config("some_decoder_type") == True
    assert _has_decoder_in_global_config("another_decoder_type") == True
    assert _has_decoder_in_global_config("nonexistent_decoder_type") == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_decoder_in_global_config_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_valid_input.py:13:4: E0401: Unable to import 'dataclasses_json_core' (import-error)


"""