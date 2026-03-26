
import pytest
from unittest.mock import patch
import cfg  # Assuming cfg is a module with global_config and encoders attributes

@pytest.mark.parametrize("invalid_type", ["invalid_type"])
def test_invalid_key(invalid_type):
    with pytest.raises(KeyError):
        with patch.dict('cfg.global_config.encoders', {k: v for k, v in cfg.global_config.encoders.items() if k != invalid_type}, clear=True):
            _get_encoder_in_global_config(invalid_type)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__get_encoder_in_global_config_1_test_invalid_key
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_1_test_invalid_key.py:4:0: E0401: Unable to import 'cfg' (import-error)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_1_test_invalid_key.py:10:12: E0602: Undefined variable '_get_encoder_in_global_config' (undefined-variable)


"""