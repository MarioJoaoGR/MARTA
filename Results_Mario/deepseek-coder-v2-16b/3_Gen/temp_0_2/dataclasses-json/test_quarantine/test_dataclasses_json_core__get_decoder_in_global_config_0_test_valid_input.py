
import pytest
from dataclasses_json.core import global_config, cfg

@pytest.fixture(autouse=True)
def setup():
    # Mocking the global configuration with decoders
    cfg.global_config.decoders = {
        'example_type': lambda x: x  # Example decoder function
    }

def test_valid_input():
    from dataclasses_json.core import _get_decoder_in_global_config
    
    # Test the function with a valid type
    decoder = _get_decoder_in_global_config('example_type')
    assert callable(decoder)  # Ensure it's a callable (decoder function)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__get_decoder_in_global_config_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_0_test_valid_input.py:3:0: E0611: No name 'global_config' in module 'dataclasses_json.core' (no-name-in-module)


"""