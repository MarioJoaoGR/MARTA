
from dataclasses_json.core import Decoder
import cfg  # Assuming cfg is a module and global_config is defined within it

def _get_decoder_in_global_config(type_):
    return cfg.global_config.decoders[type_]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__get_decoder_in_global_config_1_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_1_test_valid_input.py:2:0: E0611: No name 'Decoder' in module 'dataclasses_json.core' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_1_test_valid_input.py:3:0: E0401: Unable to import 'cfg' (import-error)


"""