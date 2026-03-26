
import pytest
from dataclasses_json.core import cfg

@pytest.fixture(autouse=True)
def setup_mock_global_config():
    # Mocking the global configuration with a sample decoder
    cfg.global_config = type('GlobalConfig', (object,), {'decoders': {}})

def test_none_input():
    with pytest.raises(KeyError):
        _get_decoder_in_global_config(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__get_decoder_in_global_config_1_test_none_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_1_test_none_input.py:12:8: E0602: Undefined variable '_get_decoder_in_global_config' (undefined-variable)


"""