
import pytest
from dataclasses_json.core import _has_encoder_in_global_config

# Mocking the necessary parts of the module for testing
class Config:
    def __init__(self):
        self.global_config = GlobalConfig()

class GlobalConfig:
    def __init__(self):
        self.encoders = {'example_encoder', 'another_example_encoder'}

cfg = Config()

def test_has_encoder_in_global_config_present():
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_encoder_in_global_config_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0.py:16:49: E0001: Parsing failed: 'expected an indented block after function definition on line 16 (Test4DT_tests.test_dataclasses_json_core__has_encoder_in_global_config_0, line 16)' (syntax-error)

"""