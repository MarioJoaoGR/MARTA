
import pytest
from unittest.mock import MagicMock
import logging
from pytutils.log import configure, get_config, DEFAULT_CONFIG

@pytest.mark.parametrize("config, env_var, default", [
    (None, 'LOGGING', {}),
    ({}, 'LOGGING', {}),
    (MagicMock(), 'LOGGING', {}),
    ('invalid config', 'LOGGING', {}),
    (None, None, None),
    (None, 'NON_EXISTENT_ENV_VAR', {}),
    (None, 'LOGGING', {'handlers': [{'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'simple'}]})
])
def test_edge_cases(config, env_var, default):
    with pytest.raises(Exception) as excinfo:
        configure(config, env_var, default)
    assert str(excinfo.value) == "Invalid logging config: None"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 7 items

../../../dev ..FF..F                                                     [100%]

=================================== FAILURES ===================================
__________________ test_edge_cases[config2-LOGGING-default2] ___________________

config = <MagicMock id='139917975539792'>, env_var = 'LOGGING', default = {}

    @pytest.mark.parametrize("config, env_var, default", [
        (None, 'LOGGING', {}),
        ({}, 'LOGGING', {}),
        (MagicMock(), 'LOGGING', {}),
        ('invalid config', 'LOGGING', {}),
        (None, None, None),
        (None, 'NON_EXISTENT_ENV_VAR', {}),
        (None, 'LOGGING', {'handlers': [{'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'simple'}]})
    ])
    def test_edge_cases(config, env_var, default):
        with pytest.raises(Exception) as excinfo:
            configure(config, env_var, default)
>       assert str(excinfo.value) == "Invalid logging config: None"
E       AssertionError: assert 'dictionary d...ify a version' == 'Invalid logging config: None'
E         
E         - Invalid logging config: None
E         + dictionary doesn't specify a version

pytutils/Test4DT_tests/test_pytutils_log_configure_2_test_edge_cases.py:19: AssertionError
_______________ test_edge_cases[invalid config-LOGGING-default3] _______________

config = 'invalid config', env_var = 'LOGGING', default = {}

    @pytest.mark.parametrize("config, env_var, default", [
        (None, 'LOGGING', {}),
        ({}, 'LOGGING', {}),
        (MagicMock(), 'LOGGING', {}),
        ('invalid config', 'LOGGING', {}),
        (None, None, None),
        (None, 'NON_EXISTENT_ENV_VAR', {}),
        (None, 'LOGGING', {'handlers': [{'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'simple'}]})
    ])
    def test_edge_cases(config, env_var, default):
        with pytest.raises(Exception) as excinfo:
            configure(config, env_var, default)
>       assert str(excinfo.value) == "Invalid logging config: None"
E       assert "load() missi...ent: 'Loader'" == 'Invalid logging config: None'
E         
E         - Invalid logging config: None
E         + load() missing 1 required positional argument: 'Loader'

pytutils/Test4DT_tests/test_pytutils_log_configure_2_test_edge_cases.py:19: AssertionError
____________________ test_edge_cases[None-LOGGING-default6] ____________________

config = None, env_var = 'LOGGING'
default = {'handlers': [{'class': 'logging.StreamHandler', 'formatter': 'simple', 'level': 'DEBUG'}]}

    @pytest.mark.parametrize("config, env_var, default", [
        (None, 'LOGGING', {}),
        ({}, 'LOGGING', {}),
        (MagicMock(), 'LOGGING', {}),
        ('invalid config', 'LOGGING', {}),
        (None, None, None),
        (None, 'NON_EXISTENT_ENV_VAR', {}),
        (None, 'LOGGING', {'handlers': [{'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'simple'}]})
    ])
    def test_edge_cases(config, env_var, default):
        with pytest.raises(Exception) as excinfo:
            configure(config, env_var, default)
>       assert str(excinfo.value) == "Invalid logging config: None"
E       AssertionError: assert 'dictionary d...ify a version' == 'Invalid logging config: None'
E         
E         - Invalid logging config: None
E         + dictionary doesn't specify a version

pytutils/Test4DT_tests/test_pytutils_log_configure_2_test_edge_cases.py:19: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-5fakyui7'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-lz7tlpvx'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-afwdduwi'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_edge_cases[config2-LOGGING-default2] - AssertionEr...
FAILED ../../../dev/::test_edge_cases[invalid config-LOGGING-default3] - asse...
FAILED ../../../dev/::test_edge_cases[None-LOGGING-default6] - AssertionError...
=================== 3 failed, 4 passed, 3 warnings in 0.09s ====================
"""