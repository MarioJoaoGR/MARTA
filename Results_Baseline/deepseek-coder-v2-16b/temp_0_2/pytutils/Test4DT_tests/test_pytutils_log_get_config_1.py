
import pytest
import os
import json
import yaml
from pytutils.log import get_config

# Test 5: Use default value if neither `given` nor `env_var` are provided
def test_get_config_default():
    config = get_config(default={'key': 'value'})
    assert config == {'key': 'value'}

# Test 6: Raise an error if config is None after all fallback mechanisms
def test_get_config_none_after_fallback():
    with pytest.raises(ValueError) as e:
        get_config()
    assert str(e.value) == "Invalid logging config: None"

# Test 7: Parse JSON string for config
def test_get_config_json():
    json_string = '{"key": "value"}'
    config = get_config(given=json_string)