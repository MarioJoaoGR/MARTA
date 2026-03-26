
import os
import pytest
from pytutils.log import get_config

# Test cases for the get_config function

def test_get_config_with_given():
    # Test case where a direct configuration value is provided
    given = '{"key": "value"}'
    env_var = None
    default = None
    
    config = get_config(given=given, env_var=env_var, default=default)
    assert isinstance(config, dict), "Expected a dictionary configuration"
    assert config == {"key": "value"}, "Expected the parsed JSON configuration to match the provided value"

def test_get_config_with_env_var():
    # Test case where an environment variable is provided and valid
    os.environ['LOG_CONFIG'] = '{"key": "value"}'
    given = None
    env_var = 'LOG_CONFIG'
    default = None
    
    config = get_config(given=given, env_var=env_var, default=default)
    assert isinstance(config, dict), "Expected a dictionary configuration"
    assert config == {"key": "value"}, "Expected the parsed JSON configuration to match the environment variable value"
    
def test_get_config_with_default():
    # Test case where a default configuration is provided
    given = None
    env_var = None
    default = {'default': 'config'}
    
    config = get_config(given=given, env_var=env_var, default=default)
    assert isinstance(config, dict), "Expected a dictionary configuration"