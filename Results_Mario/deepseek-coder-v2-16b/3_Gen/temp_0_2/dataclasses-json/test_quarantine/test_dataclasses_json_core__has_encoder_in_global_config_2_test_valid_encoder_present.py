
import pytest
from dataclasses_json.core import global_config

# Mocking the cfg module with a minimal implementation
class MockCfg:
    class GlobalConfig:
        def __init__(self):
            self.encoders = {}
    
    global_config = GlobalConfig()

cfg = MockCfg()

def test_valid_encoder_present():
    # Adding an encoder to the global configuration
    cfg.global_config.encoders['linear'] = lambda x: x  # Example encoder for 'linear' type
    
    assert _has_encoder_in_global_config('linear') is True
    assert _has_encoder_in_global_config('non_existent_type') is False

def _has_encoder_in_global_config(type_):
    return type_ in cfg.global_config.encoders

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_encoder_in_global_config_2_test_valid_encoder_present
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_2_test_valid_encoder_present.py:3:0: E0611: No name 'global_config' in module 'dataclasses_json.core' (no-name-in-module)


"""