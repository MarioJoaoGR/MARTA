
import pytest
from unittest.mock import MagicMock
from dataclasses_json.core import cfg

# Mock the global configuration and its encoders
cfg.global_config = MagicMock()
cfg.global_config.encoders = {'example_encoder': True, 'another_encoder': False}

def test_invalid_input():
    # Test with a type that is not in the global configuration
    assert not _has_encoder_in_global_config('non_existent_encoder')
    
    # Test with a type that is in the global configuration
    assert _has_encoder_in_global_config('example_encoder')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_encoder_in_global_config_0_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_invalid_input.py:12:15: E0602: Undefined variable '_has_encoder_in_global_config' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_invalid_input.py:15:11: E0602: Undefined variable '_has_encoder_in_global_config' (undefined-variable)

"""