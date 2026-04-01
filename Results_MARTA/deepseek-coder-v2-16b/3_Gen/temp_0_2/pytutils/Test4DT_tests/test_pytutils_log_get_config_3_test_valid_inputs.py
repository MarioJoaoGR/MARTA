
import pytest
import os
from pytutils.log import get_config

def test_valid_inputs():
    # Test when given is a valid JSON string
    os.environ['CONFIG'] = '{"key": "value"}'
    config = get_config(env_var='CONFIG')
    assert config == {'key': 'value'}

    # Test when given is a valid YAML string
    os.environ.pop('CONFIG', None)  # Clear the environment variable
    config = get_config(given="""{
        "another_key": "another_value"
    }""")
    assert config == {'another_key': 'another_value'}

    # Test when default is provided and valid JSON
    config = get_config(default='{"final_key": "final_value"}')
    assert config == {'final_key': 'final_value'}

    # Test when none of the inputs are provided, should raise ValueError
    with pytest.raises(ValueError):
        get_config()
