
import pytest
from dataclasses_json.core import _has_decoder_in_global_config

# Mocking the necessary parts of the module for testing
class Config:
    global_config = {
        'decoders': ['example_decoder', 'another_decoder']
    }

cfg = Config()

def test_existing_decoder():
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_decoder_in_global_config_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0.py:13:29: E0001: Parsing failed: 'expected an indented block after function definition on line 13 (Test4DT_tests.test_dataclasses_json_core__has_decoder_in_global_config_0, line 13)' (syntax-error)

"""