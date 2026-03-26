
import pytest
from dataclasses_json.core import cfg

@pytest.fixture(autouse=True)
def setup_mock_config():
    # Mock the global configuration with a sample encoders dictionary
    cfg.global_config = type('GlobalConfig', (object,), {'encoders': {}})

def test_invalid_encoder_type():
    assert not _has_encoder_in_global_config('non_existent_type')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_encoder_in_global_config_2_test_invalid_encoder_type
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_2_test_invalid_encoder_type.py:11:15: E0602: Undefined variable '_has_encoder_in_global_config' (undefined-variable)


"""