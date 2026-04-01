
import pytest
from dataclasses_json import core as cfg

def _get_decoder_in_global_config(type_):
    return cfg.global_config.decoders[type_]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__get_decoder_in_global_config_0_test_none_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_0_test_none_input.py:6:11: E1101: Module 'dataclasses_json.core' has no 'global_config' member (no-member)


"""