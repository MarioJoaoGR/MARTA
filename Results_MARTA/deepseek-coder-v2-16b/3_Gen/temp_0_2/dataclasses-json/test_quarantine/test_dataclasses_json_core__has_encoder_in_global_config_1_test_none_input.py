
import pytest
from dataclasses_json.core import cfg

@pytest.fixture(autouse=True)
def setup():
    # Mock global configuration with an encoder
    cfg.global_config.encoders = {'linear': lambda x: x}

def test_none_input():
    assert not _has_encoder_in_global_config('non_existent_type')
    assert _has_encoder_in_global_config('linear')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_encoder_in_global_config_1_test_none_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_1_test_none_input.py:11:15: E0602: Undefined variable '_has_encoder_in_global_config' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_1_test_none_input.py:12:11: E0602: Undefined variable '_has_encoder_in_global_config' (undefined-variable)


"""