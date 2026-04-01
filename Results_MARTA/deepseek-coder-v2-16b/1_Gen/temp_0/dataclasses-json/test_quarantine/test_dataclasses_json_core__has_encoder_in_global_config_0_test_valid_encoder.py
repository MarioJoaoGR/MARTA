
import pytest
from dataclasses_json import core as cfg  # Assuming 'core' is the module where cfg is defined

# Mocking the global configuration object and its encoders attribute
class MockConfig:
    def __init__(self):
        self.encoders = {}

@pytest.fixture(autouse=True)
def mock_config():
    # Create a mock for the config module
    cfg.global_config = MockConfig()

# Test case to check if an encoder is present in the global configuration
def test_valid_encoder():
    # Add an encoder to the mocked global configuration
    cfg.global_config.encoders['example_encoder'] = lambda x: x  # Example encoder function
    
    # Check if the encoder is present
    assert _has_encoder_in_global_config('example_encoder') == True
    
    # Remove the added encoder to ensure it's not there for other tests
    del cfg.global_config.encoders['example_encoder']

# Run the test case
if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_encoder_in_global_config_0_test_valid_encoder
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_valid_encoder.py:21:11: E0602: Undefined variable '_has_encoder_in_global_config' (undefined-variable)

"""