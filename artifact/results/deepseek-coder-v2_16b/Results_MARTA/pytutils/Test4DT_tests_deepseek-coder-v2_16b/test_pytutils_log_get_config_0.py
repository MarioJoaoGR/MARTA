
import pytest
import os
from pytutils.log import get_config

# Test case for providing all parameters directly
def test_get_config_with_all_parameters():
    given = '{"key": "value"}'
    env_var = 'LOG_CONFIG'
    default = {}
    
    os.environ[env_var] = given
    config = get_config(given=given, env_var=env_var, default=default)
    
    assert isinstance(config, dict)
    assert config == {'key': 'value'}

# Test case for using environment variable if provided
def test_get_config_with_env_var():
    given = None
    env_var = 'LOG_CONFIG'
    default = {}
    
    os.environ[env_var] = '{"key": "value"}'
    config = get_config(given=given, env_var=env_var, default=default)
    
    assert isinstance(config, dict)
    assert config == {'key': 'value'}

# Test case for providing only the default parameter
def test_get_config_with_default():
    given = None
    env_var = None
    default = {'key': 'value'}
    
    config = get_config(given=given, env_var=env_var, default=default)
    
    assert isinstance(config, dict)
    assert config == {'key': 'value'}

# Test case for handling invalid configuration
def test_get_config_invalid_configuration():
    given = None
    env_var = None
    default = None
    
    with pytest.raises(ValueError):
        get_config(given=given, env_var=env_var, default=default)
