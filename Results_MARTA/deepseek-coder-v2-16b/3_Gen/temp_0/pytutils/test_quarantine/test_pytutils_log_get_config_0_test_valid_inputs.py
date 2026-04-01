
import os
import pytest
import json
import yaml
from pytutils.log import get_config

@pytest.mark.parametrize("given, env_var, default, expected", [
    ('{"key": "value"}', None, None, {'key': 'value'}),
    (None, 'LOG_CONFIG', {'default': 'config'}, {'default': 'config'}),
    (None, 'LOG_CONFIG', None, ValueError),
    ('invalid json', None, None, ValueError),
    ('--- !some-format\nkey: value', None, None, {'key': 'value'})
])
def test_valid_inputs(monkeypatch, given, env_var, default, expected):
    if isinstance(expected, dict):
        monkeypatch.setenv('LOG_CONFIG', json.dumps({'key': 'value'}))
    elif isinstance(expected, ValueError):
        with pytest.raises(ValueError):
            get_config(given=given, env_var=env_var, default=default)
    else:
        with pytest.raises(ValueError):
            get_config(given=given, env_var=env_var, default=default)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""