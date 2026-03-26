
import pytest
import os
import json
import yaml
from pytutils.log import get_config

# Test 1: Retrieve configuration from an environment variable
def test_get_config_env_var():
    os.environ['CONFIG'] = '{"key": "value"}'
    config = get_config(env_var='CONFIG')
    assert config == {'key': 'value'}

# Test 2: Retrieve configuration directly from a provided dictionary
def test_get_config_given():
    config = get_config(given={'key': 'value'})
    assert config == {'key': 'value'}

# Test 3: Raise an error if neither `given` nor `env_var` are provided
def test_get_config_none():
    with pytest.raises(ValueError) as e:
        get_config()
    assert str(e.value) == "Invalid logging config: None"

# Test 4: Retrieve configuration from a JSON string
def test_get_config_json_string():
    json_string = '{"key": "value"}'
    config = get_config(given=json_string)