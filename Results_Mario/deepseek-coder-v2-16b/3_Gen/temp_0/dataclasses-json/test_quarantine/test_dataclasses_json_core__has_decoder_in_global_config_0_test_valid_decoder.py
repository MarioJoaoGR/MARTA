
import pytest
from dataclasses_json.core import cfg  # Assuming 'cfg' is defined in this module

# Mocking the necessary parts of the system
class MockConfig:
    def __init__(self):
        self.decoders = []
    
    def add_decoder(self, decoder):
        if decoder not in self.decoders:
            self.decoders.append(decoder)

# Fixture to set up the mock configuration
@pytest.fixture
def setup_mock_config():
    cfg.global_config = MockConfig()

def test_valid_decoder(setup_mock_config):
    # Adding a decoder to the mock config
    cfg.global_config.add_decoder('example_decoder')
    
    # Checking if the added decoder is in the global configuration
    has_decoder = _has_decoder_in_global_config('example_decoder')
    
    assert has_decoder is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_decoder_in_global_config_0_test_valid_decoder
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_valid_decoder.py:24:18: E0602: Undefined variable '_has_decoder_in_global_config' (undefined-variable)


"""