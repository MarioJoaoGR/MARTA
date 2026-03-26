
import os
import pytest
from pytutils.log import get_config

# Mocking os.environ for testing purposes
@pytest.fixture(autouse=True)
def mock_os_env():
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(os, 'environ', {})
        yield

def test_get_config_with_given():
    config = get_config(given='{"key": "value"}')
    assert isinstance(config, dict)
    assert config == {'key': 'value'}

def test_get_config_with_env_var():
    os.environ['LOG_CONFIG'] = '{"key": "value"}'
    config = get_config(env_var='LOG_CONFIG')
    assert isinstance(config, dict)
    assert config == {'key': 'value'}
    del os.environ['LOG_CONFIG']

def test_get_config_with_default():
    config = get_config(default={'default': 'config'})
    assert isinstance(config, dict)
    assert config == {'default': 'config'}

def test_get_config_invalid_input():
    with pytest.raises(ValueError):
        get_config()

def test_get_config_invalid_json():
    with pytest.raises(ValueError):
        get_config(given='{invalid: json}')

def test_get_config_invalid_yaml():
    with pytest.raises(ValueError):
        get_config(given="""name: Mario""")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""