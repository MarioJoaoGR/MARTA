
import pytest
from dataclasses_json.core import global_config

def _has_decoder_in_global_config(type_):
    return type_ in global_config.decoders

# Test to check if the function correctly identifies a missing decoder in the global configuration
def test_missing_decoder():
    assert not _has_decoder_in_global_config("nonexistent_decoder_type")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_decoder_in_global_config_1_test_missing_decoder
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_1_test_missing_decoder.py:3:0: E0611: No name 'global_config' in module 'dataclasses_json.core' (no-name-in-module)


"""