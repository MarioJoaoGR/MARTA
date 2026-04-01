
import pytest
from dataclasses_json.core import cfg  # Assuming this is where the global config is defined

# Mocking the global configuration and its decoders for testing purposes
class MockConfig:
    def __init__(self):
        self.decoders = {
            'some_type': lambda x: f"Decoded {x}"
        }

cfg.global_config = MockConfig()

def test_none_input():
    with pytest.raises(KeyError):
        assert _get_decoder_in_global_config('non_existent_type') is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__get_decoder_in_global_config_2_test_none_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_2_test_none_input.py:16:15: E0602: Undefined variable '_get_decoder_in_global_config' (undefined-variable)


"""