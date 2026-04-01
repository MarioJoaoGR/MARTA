
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

@pytest.mark.parametrize("given, env_var, default, expected", [
    ({"key": "value"}, None, None, {"key": "value"}),
    (None, 'CONFIG', None, {'key': 'value'}),
    (None, None, {'default_key': 'default_value'}, {'default_key': 'default_value'}),
    ('{"key": "value"}', None, None, {"key": "value"}),
    ('invalid_json', None, None, ValueError),
    ('!@#$%^&*()', None, None, ValueError),
])
def test_edge_cases(given, env_var, default, expected):
    if env_var:
        with patch.dict('os.environ', {env_var: '{"key": "value"}'}):
            if isinstance(expected, dict):
                assert get_config(given=given, env_var=env_var) == expected
            else:
                with pytest.raises(ValueError):
                    get_config(given=given, env_var=env_var)
    elif default:
        if isinstance(expected, dict):
            assert get_config(default=default) == expected
        else:
            with pytest.raises(ValueError):
                get_config(default=default)
    else:
        if isinstance(given, dict):
            assert get_config(given=given) == given
        elif isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                get_config()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_log_get_config_2_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_edge_cases.py:25:25: E1120: No value for argument 'Loader' in function call (no-value-for-parameter)


"""