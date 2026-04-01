
import os
import json
import yaml
import pytest
from pytutils.log import get_config

def test_edge_cases():
    # Test with None values
    assert get_config(given=None, env_var=None, default=None) is None
    
    # Test with empty string
    assert get_config(given='', env_var=None, default=None) == ''
    
    # Test with empty dictionary
    assert get_config(given={}, env_var=None, default=None) == {}
    
    # Test with invalid JSON string
    with pytest.raises(ValueError):
        get_config(given='invalid json', env_var=None, default=None)
    
    # Test with valid JSON string
    config = '{"key": "value"}'
    assert get_config(given=config, env_var=None, default=None) == {'key': 'value'}
    
    # Test with invalid YAML string
    with pytest.raises(ValueError):
        get_config(given='invalid yaml', env_var=None, default=None)
    
    # Test with valid YAML string
    config = """
    key: value
    """
    assert get_config(given=config, env_var=None, default=None) == {'key': 'value'}
    
    # Test with environment variable
    os.environ['LOG_CONFIG'] = '{"env": "value"}'
    assert get_config(env_var='LOG_CONFIG') == {'env': 'value'}
    
    # Test with default value
    assert get_config(env_var=None, default={'default': 'config'}) == {'default': 'config'}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

../../../dev F                                                           [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test with None values
>       assert get_config(given=None, env_var=None, default=None) is None

pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_edge_cases.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

given = None, env_var = None, default = None

    def get_config(given=None, env_var=None, default=None):
        config = given
    
        if not config and env_var:
            config = os.environ.get(env_var)
    
        if not config and default:
            config = default
    
        if config is None:
>           raise ValueError('Invalid logging config: %s' % config)
E           ValueError: Invalid logging config: None

pytutils/pytutils/log.py:114: ValueError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-qfp7w50v'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-naomi7tx'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-_nalqheq'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_edge_cases - ValueError: Invalid logging config: None
======================== 1 failed, 3 warnings in 0.11s =========================
"""