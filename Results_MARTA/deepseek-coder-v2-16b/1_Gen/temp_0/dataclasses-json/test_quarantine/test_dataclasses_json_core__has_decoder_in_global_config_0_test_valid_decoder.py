
import pytest
from dataclasses_json.core import global_config  # Assuming this is the correct module path

# Mocking the cfg object with a global_config attribute containing a decoders dictionary
class MockConfig:
    def __init__(self):
        self.global_config = MockGlobalConfig()

class MockGlobalConfig:
    def __init__(self):
        self.decoders = {'example_decoder': True}  # Example decoder for testing

# Fixture to provide the mock config object
@pytest.fixture
def mock_config():
    return MockConfig()

def test_valid_decoder(mock_config):
    assert _has_decoder_in_global_config('example_decoder', mock_config) is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_decoder_in_global_config_0_test_valid_decoder
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_valid_decoder.py:3:0: E0611: No name 'global_config' in module 'dataclasses_json.core' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_valid_decoder.py:20:11: E0602: Undefined variable '_has_decoder_in_global_config' (undefined-variable)

"""