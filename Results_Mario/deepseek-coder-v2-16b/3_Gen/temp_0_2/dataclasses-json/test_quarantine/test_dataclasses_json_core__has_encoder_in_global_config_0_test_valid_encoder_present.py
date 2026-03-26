
import pytest
from dataclasses_json.core import cfg

@pytest.fixture(autouse=True)
def setup():
    # Mock global configuration with a sample encoder
    cfg.global_config = type('GlobalConfig', (object,), {'encoders': {}})

def test_valid_encoder_present():
    # Add an encoder to the global config
    cfg.global_config.encoders['linear'] = lambda x: x  # Example encoder for 'linear'
    
    assert _has_encoder_in_global_config('linear') is True
    assert _has_encoder_in_global_config('non_existent_type') is False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_encoder_in_global_config_0_test_valid_encoder_present
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_valid_encoder_present.py:14:11: E0602: Undefined variable '_has_encoder_in_global_config' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_valid_encoder_present.py:15:11: E0602: Undefined variable '_has_encoder_in_global_config' (undefined-variable)


"""