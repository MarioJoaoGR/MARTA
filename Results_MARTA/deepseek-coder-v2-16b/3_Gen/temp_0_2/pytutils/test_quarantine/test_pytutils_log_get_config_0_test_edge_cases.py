
import pytest
import os
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
                config = yaml.load(config)
            except ValueError:
                raise ValueError("Could not parse logging config as bare, json, or yaml: %s" % config)

    return config

@pytest.mark.parametrize("given, env_var, default", [
    (None, 'CONFIG', {'default_key': 'default_value'}),
    ({}, 'CONFIG', None),
    ('{"key": "value"}', None, None),
    ('invalid json', None, None),
    ('---', None, None)
])
def test_edge_cases(given, env_var, default):
    with patch.dict(os.environ, {env_var: '{"key": "value}"' if isinstance(given, str) else ''}):
        if given is None and env_var not in os.environ:
            with pytest.raises(ValueError):
                get_config(given=given, env_var=env_var, default=default)
        else:
            config = get_config(given=given, env_var=env_var, default=default)
            if isinstance(given, dict) or (given is None and env_var in os.environ):
                assert config == {'key': 'value'}
            elif given is None and not os.environ.get(env_var):
                assert config == {'default_key': 'default_value'}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_log_get_config_0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_log_get_config_0_test_edge_cases.py:25:25: E1120: No value for argument 'Loader' in function call (no-value-for-parameter)


"""