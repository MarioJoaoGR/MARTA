
import pytest
from dataclasses_json.core import cfg  # Assuming this is the correct module path

# Mocking the global configuration with encoders dictionary
class MockConfig:
    def __init__(self):
        self.encoders = {
            'some_type': lambda x: x,
            'another_type': lambda y: y
        }

@pytest.fixture(autouse=True)
def mock_cfg():
    cfg.global_config = MockConfig()

# Test case for invalid key
def test_invalid_key():
    with pytest.raises(KeyError):
        _get_encoder_in_global_config('invalid_type')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__get_encoder_in_global_config_1_test_invalid_key
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_1_test_invalid_key.py:20:8: E0602: Undefined variable '_get_encoder_in_global_config' (undefined-variable)


"""