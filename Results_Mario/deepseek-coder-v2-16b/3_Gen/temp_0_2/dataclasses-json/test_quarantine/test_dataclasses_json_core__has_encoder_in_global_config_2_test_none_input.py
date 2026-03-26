
import pytest
from dataclasses_json.core import cfg

@pytest.fixture(autouse=True)
def setup():
    # Mock global configuration with an empty dictionary
    cfg.global_config = type('GlobalConfig', (object,), {'encoders': {}})()

def test_none_input():
    assert not _has_encoder_in_global_config(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_encoder_in_global_config_2_test_none_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_2_test_none_input.py:11:15: E0602: Undefined variable '_has_encoder_in_global_config' (undefined-variable)


"""