
import pytest
from dataclasses_json.core import global_config  # Importing from the correct module

# Mocking cfg object with necessary attributes
class MockCfg:
    class MockGlobalConfig:
        def __init__(self, decoders):
            self.decoders = decoders
    
    global_config = MockGlobalConfig({'example_decoder': None})  # Initialize with a mock dictionary

# Test case for _has_decoder_in_global_config function
def test_missing_decoder():
    assert not _has_decoder_in_global_config('missing_decoder')  # Check if 'missing_decoder' is not in the global config

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_decoder_in_global_config_0_test_missing_decoder
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_missing_decoder.py:3:0: E0611: No name 'global_config' in module 'dataclasses_json.core' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_missing_decoder.py:15:15: E0602: Undefined variable '_has_decoder_in_global_config' (undefined-variable)

"""