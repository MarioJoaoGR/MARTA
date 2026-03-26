
import os
import pytest
import json
import yaml
from unittest.mock import patch

def get_config(given=None, env_var=None, default=None):
    config = given

    if not config and env_var:
        config = os.environ.get(env_var)

    if not config and default:
        config = default

    if config is None:
        raise ValueError('Invalid logging config: %s' % config)

    if isinstance(config, str):
        try:
            config = json.loads(config)
        except ValueError:
            try:
                config = yaml.load(config, Loader=yaml.FullLoader)
            except ValueError:
                raise ValueError("Could not parse logging config as bare, json, or yaml: %s" % config)

    return config

@pytest.fixture(autouse=True)
def setup_env():
    os.environ['CONFIG'] = '{"key": "value"}'

def test_valid_inputs():
    with patch('os.environ', {'CONFIG': json.dumps({"key": "value"})}):
        config = get_config(env_var='CONFIG')
        assert config == {"key": "value"}

        config = get_config(given={"key": "value"})
        assert config == {"key": "value"}

        config = get_config(default={"default_key": "default_value"})
        assert config == {"default_key": "default_value"}
