
import pytest
from dataclasses_json.core import cfg  # Assuming 'cfg' is a module-level configuration object

# Mocking the necessary parts of the global configuration
class MockGlobalConfig:
    encoders = {
        'some_type': lambda x: x,  # Example encoder function
        'another_type': lambda y: y
    }

def test_get_encoder_in_global_config():
    # Set up the mock configuration object
    cfg.global_config = MockGlobalConfig()
    
    # Test retrieving a valid encoder
    assert _get_encoder_in_global_config('some_type') == cfg.global_config.encoders['some_type']
    
    # Test retrieving an invalid encoder to ensure it raises an appropriate error or returns a default value as configured
    with pytest.raises(KeyError):  # Adjust the exception type if different is expected
        _get_encoder_in_global_config('invalid_type')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__get_encoder_in_global_config_2_test_invalid_key
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_2_test_invalid_key.py:17:11: E0602: Undefined variable '_get_encoder_in_global_config' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_2_test_invalid_key.py:21:8: E0602: Undefined variable '_get_encoder_in_global_config' (undefined-variable)

"""