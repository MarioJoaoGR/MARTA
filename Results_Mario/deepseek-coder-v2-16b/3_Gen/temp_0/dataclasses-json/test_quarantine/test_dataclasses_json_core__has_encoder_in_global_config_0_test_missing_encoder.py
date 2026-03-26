
from dataclasses_json.core import Config

def _has_encoder_in_global_config(type_):
    return type_ in cfg.global_config.encoders

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_encoder_in_global_config_0_test_missing_encoder
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_missing_encoder.py:2:0: E0611: No name 'Config' in module 'dataclasses_json.core' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_missing_encoder.py:5:20: E0602: Undefined variable 'cfg' (undefined-variable)


"""