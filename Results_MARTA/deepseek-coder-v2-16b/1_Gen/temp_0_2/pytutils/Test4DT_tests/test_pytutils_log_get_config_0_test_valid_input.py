
import os
import pytest
import json
import yaml
from pytutils.log import get_config

@pytest.fixture(autouse=True)
def setup():
    os.environ['CONFIG'] = '{"key": "value"}'

def test_valid_input():
    config = get_config(env_var='CONFIG')
    assert config == {"key": "value"}
