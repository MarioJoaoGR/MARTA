
import pytest
from dataclasses_json.core import Config

# Mocking the cfg object with global_config attribute containing encoders
class MockCfg:
    class GlobalConfig:
        def __init__(self, encoders=None):
            self.encoders = encoders if encoders is not None else {}

@pytest.fixture
def mock_cfg():
    return MockCfg()

# Test case to check for the presence of an encoder in global configuration
def test_missing_encoder(mock_cfg):
    # Create a Config object with no initial encoders
    cfg = mock_cfg
    assert not _has_encoder_in_global_config('example_encoder')

# Function to be tested
def _has_encoder_in_global_config(type_):
    return type_ in cfg.global_config.encoders

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_encoder_in_global_config_0_test_missing_encoder
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_missing_encoder.py:3:0: E0611: No name 'Config' in module 'dataclasses_json.core' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_missing_encoder.py:23:20: E0602: Undefined variable 'cfg' (undefined-variable)

"""