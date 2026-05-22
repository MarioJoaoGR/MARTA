
import pytest
from unittest.mock import patch
from httpie.config import __version__

@pytest.mark.parametrize("meta, expected", [
    ({}, __version__),
    ({'httpie': '1.0.3'}, '1.0.3'),
])
def test_version(meta, expected):
    with patch('httpie.config.__version__', '1.0.3'):
        config = BaseConfigDict(path='/some/file/path')
        config.get = lambda section, default: meta.get(section, default)
        assert config.version() == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_config_BaseConfigDict_version_2_test_invalid_inputs
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_BaseConfigDict_version_2_test_invalid_inputs.py:12:17: E0602: Undefined variable 'BaseConfigDict' (undefined-variable)


"""