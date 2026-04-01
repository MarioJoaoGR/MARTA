
import os
from pytutils.log import get_config

def test_get_config_with_env_var():
    # Ensure the env var is not set initially
    os.environ.pop('CONFIG', None)
    
    # Test with default value
    config = get_config(default={'key': 'value'})
    assert config == {'key': 'value'}
    
    # Set the env var and test again
    os.environ['CONFIG'] = '{"env_key": "env_value"}'
    config = get_config(env_var='CONFIG')
    assert config == {'env_key': 'env_value'}
