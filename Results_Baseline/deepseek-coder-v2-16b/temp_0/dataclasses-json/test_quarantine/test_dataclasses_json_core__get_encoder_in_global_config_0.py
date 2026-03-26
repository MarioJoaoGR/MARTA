
# Module: dataclasses_json.core
import pytest
from your_module_name import _get_encoder_in_global_config  # Replace 'your_module_name' with the actual module name

# Mocking the necessary parts of the configuration for testing
class Config:
    def __init__(self):
        self.global_config = GlobalConfig()

class GlobalConfig:
    def __init__(self):
        self.encoders = {
            'some_type': "EncoderForSomeType",
            'another_type': "EncoderForAnotherType"
        }

# Mocking the cfg object for testing
cfg = Config()

def test_get_encoder_in_global_config_basic():
    encoder = _get_encoder_in_global_config('some_type')
    assert encoder == "EncoderForSomeType"

def test_get_encoder_in_global_config_default():
    encoder = _get_encoder_in_global_config('another_type')
    assert encoder == "EncoderForAnotherType"

def test_get_encoder_in_global_config_error():
    with pytest.raises(KeyError):
        _get_encoder_in_global_config('non_existent_type')

def test_get_encoder_in_global_config_conditional():
    cfg.global_config.encoders = {}  # Emulate a missing type in configuration
    with pytest.raises(KeyError):
        _get_encoder_in_global_config('specific_type')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__get_encoder_in_global_config_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_0.py:4:0: E0401: Unable to import 'your_module_name' (import-error)

"""