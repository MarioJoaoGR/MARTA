
import pytest
import os
from pytutils.log import get_config

def test_get_config_with_given():
    given = '{"key": "value"}'
    config = get_config(given=given)
    assert isinstance(config, dict)
    assert config['key'] == 'value'

def test_get_config_with_env_var():
    os.environ['LOG_CONFIG'] = '{"env_key": "env_value"}'
    config = get_config(env_var='LOG_CONFIG')
    assert isinstance(config, dict)
    assert config['env_key'] == 'env_value'
    del os.environ['LOG_CONFIG']

def test_get_config_with_default():
    default = {'default_key': 'default_value'}
    config = get_config(default=default)
    assert isinstance(config, dict)
    assert config['default_key'] == 'default_value'
