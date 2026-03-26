
from dataclasses_json.core import global_config

def _has_decoder_in_global_config(type_):
    return type_ in global_config.decoders

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_decoder_in_global_config_0_test_invalid_input_type
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_invalid_input_type.py:2:0: E0611: No name 'global_config' in module 'dataclasses_json.core' (no-name-in-module)


"""