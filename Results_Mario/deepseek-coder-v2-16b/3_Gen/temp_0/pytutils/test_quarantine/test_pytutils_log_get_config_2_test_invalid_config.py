
import pytest
import os
from pytutils.log import get_config

def test_invalid_config():
    with pytest.raises(ValueError, match="Could not parse logging config as bare, json, or yaml: invalid"):
        get_config()

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
_____________________________ test_invalid_config ______________________________

    def test_invalid_config():
        with pytest.raises(ValueError, match="Could not parse logging config as bare, json, or yaml: invalid"):
>           get_config()

pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_invalid_config.py:8: 
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

During handling of the above exception, another exception occurred:

    def test_invalid_config():
>       with pytest.raises(ValueError, match="Could not parse logging config as bare, json, or yaml: invalid"):
E       AssertionError: Regex pattern did not match.
E        Regex: 'Could not parse logging config as bare, json, or yaml: invalid'
E        Input: 'Invalid logging config: None'

pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_invalid_config.py:7: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-v7i2moyz'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-lwtsewh6'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-vhn1is6d'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_invalid_config - AssertionError: Regex pattern did...
======================== 1 failed, 3 warnings in 0.06s =========================
"""