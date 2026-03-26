
import pytest
from dataclasses_json.core import _get_encoder_in_global_config
from unittest.mock import patch

# Mocking the cfg module and its global_config with encoders dictionary
@patch('dataclasses_json.core.cfg')
def test_none_input(_):
    # Define a mock for the global_config object
    class MockGlobalConfig:
        encoders = {'some_type': 'mocked_encoder'}
    
    cfg.global_config = MockGlobalConfig()
    
    # Test when type is provided as None
    with pytest.raises(KeyError):
        _get_encoder_in_global_config(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__get_encoder_in_global_config_1_test_none_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_1_test_none_input.py:13:4: E0602: Undefined variable 'cfg' (undefined-variable)


"""