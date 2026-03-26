
import os
import pytest
import json
import yaml
from pytutils.log import get_config

@pytest.mark.parametrize("given, env_var, default", [
    (None, 'INVALID_ENV', None),  # Both given and env_var are invalid
    ('{"key": "value"}', 'INVALID_ENV', None),  # Only given is valid, env_var is invalid
    (None, 'LOG_CONFIG', {'default': 'config'}),  # Only env_var is valid, default is not provided
])
def test_invalid_inputs(given, env_var, default):
    with pytest.raises(ValueError) as excinfo:
        get_config(given=given, env_var=env_var, default=default)
    assert str(excinfo.value) == 'Invalid logging config: %s' % (given if given else env_var if env_var else default)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

../../../dev FFF                                                         [100%]

=================================== FAILURES ===================================
__________________ test_invalid_inputs[None-INVALID_ENV-None] __________________

given = None, env_var = 'INVALID_ENV', default = None

    @pytest.mark.parametrize("given, env_var, default", [
        (None, 'INVALID_ENV', None),  # Both given and env_var are invalid
        ('{"key": "value"}', 'INVALID_ENV', None),  # Only given is valid, env_var is invalid
        (None, 'LOG_CONFIG', {'default': 'config'}),  # Only env_var is valid, default is not provided
    ])
    def test_invalid_inputs(given, env_var, default):
        with pytest.raises(ValueError) as excinfo:
            get_config(given=given, env_var=env_var, default=default)
>       assert str(excinfo.value) == 'Invalid logging config: %s' % (given if given else env_var if env_var else default)
E       AssertionError: assert 'Invalid logging config: None' == 'Invalid logg...: INVALID_ENV'
E         
E         - Invalid logging config: INVALID_ENV
E         ?                         - ^^^^^^^^^
E         + Invalid logging config: None
E         ?                          ^^^

pytutils/Test4DT_tests/test_pytutils_log_get_config_3_test_invalid_inputs.py:16: AssertionError
____________ test_invalid_inputs[{"key": "value"}-INVALID_ENV-None] ____________

given = '{"key": "value"}', env_var = 'INVALID_ENV', default = None

    @pytest.mark.parametrize("given, env_var, default", [
        (None, 'INVALID_ENV', None),  # Both given and env_var are invalid
        ('{"key": "value"}', 'INVALID_ENV', None),  # Only given is valid, env_var is invalid
        (None, 'LOG_CONFIG', {'default': 'config'}),  # Only env_var is valid, default is not provided
    ])
    def test_invalid_inputs(given, env_var, default):
>       with pytest.raises(ValueError) as excinfo:
E       Failed: DID NOT RAISE <class 'ValueError'>

pytutils/Test4DT_tests/test_pytutils_log_get_config_3_test_invalid_inputs.py:14: Failed
________________ test_invalid_inputs[None-LOG_CONFIG-default2] _________________

given = None, env_var = 'LOG_CONFIG', default = {'default': 'config'}

    @pytest.mark.parametrize("given, env_var, default", [
        (None, 'INVALID_ENV', None),  # Both given and env_var are invalid
        ('{"key": "value"}', 'INVALID_ENV', None),  # Only given is valid, env_var is invalid
        (None, 'LOG_CONFIG', {'default': 'config'}),  # Only env_var is valid, default is not provided
    ])
    def test_invalid_inputs(given, env_var, default):
>       with pytest.raises(ValueError) as excinfo:
E       Failed: DID NOT RAISE <class 'ValueError'>

pytutils/Test4DT_tests/test_pytutils_log_get_config_3_test_invalid_inputs.py:14: Failed
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-20_cw525'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-fnveh6p0'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-fapcw77v'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_invalid_inputs[None-INVALID_ENV-None] - AssertionE...
FAILED ../../../dev/::test_invalid_inputs[{"key": "value"}-INVALID_ENV-None]
FAILED ../../../dev/::test_invalid_inputs[None-LOG_CONFIG-default2] - Failed:...
======================== 3 failed, 3 warnings in 0.10s =========================
"""