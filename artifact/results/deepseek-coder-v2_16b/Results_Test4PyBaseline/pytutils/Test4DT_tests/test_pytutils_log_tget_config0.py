
import pytest
import os
from pytutils.log import get_config
import json
import yaml

# Test cases for get_config function

def test_get_config_with_given():
    given = {"key": "value"}
    config = get_config(given=given)
    assert config == given

def test_get_config_with_env_var():
    os.environ['CONFIG'] = json.dumps({"key": "value"})
    config = get_config(env_var='CONFIG')