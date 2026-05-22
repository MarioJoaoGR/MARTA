
import pytest
from unittest.mock import patch
from httpie.config import __version__
from httpie_config import BaseConfigDict

@pytest.fixture
def config():
    return BaseConfigDict(path='/some/file/path')

def test_version_default(config):
    with patch('httpie.config.__version__', '1.0.0'):
        assert config.version() == '1.0.0'

def test_version_specified(config):
    with patch('httpie.config.__version__', '1.0.0'):
        config._data['__meta__'] = {'httpie': '2.0.0'}
        assert config.version() == '2.0.0'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_config_BaseConfigDict_version_3_test_edge_cases
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_BaseConfigDict_version_3_test_edge_cases.py:5:0: E0401: Unable to import 'httpie_config' (import-error)


"""