
import os
import json
import yaml
from pytutils.log import get_config
import pytest
from unittest.mock import patch, MagicMock

def test_get_config_with_given():
    given = '{"key": "value"}'
    config = get_config(given=given)
    assert isinstance(config, dict)
    assert config == {'key': 'value'}

def test_get_config_with_env_var():
    with patch.dict('os.environ', {'LOG_CONFIG': '{"key": "value"}'}):
        config = get_config(env_var='LOG_CONFIG')
        assert isinstance(config, dict)
        assert config == {'key': 'value'}

def test_get_config_with_default():
    default = {'default': 'config'}
    config = get_config(default=default)
    assert isinstance(config, dict)
    assert config == {'default': 'config'}

def test_get_config_invalid_format():
    with pytest.raises(ValueError):
        invalid_config = "invalid configuration"
        get_config(given=invalid_config)

def test_get_config_env_var_and_default():
    with patch.dict('os.environ', {'LOG_CONFIG': '{"key": "value"}'}):
        config = get_config(env_var='LOG_CONFIG', default={'default': 'config'})
        assert isinstance(config, dict)
        assert config == {'key': 'value'}

def test_get_config_invalid_json():
    invalid_json = '{"key": "value'  # Missing closing brace
    with pytest.raises(ValueError):
        get_config(given=invalid_json)

def test_get_config_invalid_yaml():
    invalid_yaml = "- key: value"  # Incorrect YAML format
    with pytest.raises(ValueError):
        get_config(given=invalid_yaml)

def test_get_config_no_source():
    with pytest.raises(ValueError):
        get_config()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""