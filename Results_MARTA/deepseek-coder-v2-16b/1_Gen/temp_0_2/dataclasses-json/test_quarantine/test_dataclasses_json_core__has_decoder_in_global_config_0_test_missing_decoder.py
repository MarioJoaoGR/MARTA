
import pytest
from dataclasses_json.core import _has_decoder_in_global_config

# Mocking the cfg object with global_config attribute containing a decoders set
class MockConfig:
    class GlobalConfig:
        def __init__(self, decoders):
            self.decoders = decoders

@pytest.fixture
def mock_cfg():
    return MockConfig(GlobalConfig({'example_decoder': True}))

def test_missing_decoder(mock_cfg):
    assert _has_decoder_in_global_config('non_existent_decoder', cfg=mock_cfg) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_decoder_in_global_config_0_test_missing_decoder
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_missing_decoder.py:13:22: E0602: Undefined variable 'GlobalConfig' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_missing_decoder.py:16:11: E1123: Unexpected keyword argument 'cfg' in function call (unexpected-keyword-arg)


"""