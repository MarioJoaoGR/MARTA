
import pytest
from dataclasses_json.core import Decoder  # Assuming this is the correct module path

# Mocking the global configuration store
class GlobalConfigMock:
    def __init__(self):
        self.decoders = {
            'some_type': "decoder_for_some_type"
        }

cfg = GlobalConfigMock()  # Create an instance of the mock config

def _get_decoder_in_global_config(type_):
    return cfg.global_config.decoders[type_]

# Test case for valid input
def test_valid_input():
    type_ = 'some_type'
    result = _get_decoder_in_global_config(type_)
    assert result == "decoder_for_some_type"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__get_decoder_in_global_config_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_0_test_valid_input.py:3:0: E0611: No name 'Decoder' in module 'dataclasses_json.core' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_0_test_valid_input.py:15:11: E1101: Instance of 'GlobalConfigMock' has no 'global_config' member (no-member)


"""