
import pytest
from pytutils.log import configure, DEFAULT_CONFIG
import logging

@pytest.fixture(autouse=True)
def setup():
    # Reset logging configuration before each test
    logging.config.dictConfig({})

def test_valid_inputs():
    log = logging.getLogger(__name__)
    configure()
    log.info('test')

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

../../../dev E                                                           [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_valid_inputs ______________________

    @pytest.fixture(autouse=True)
    def setup():
        # Reset logging configuration before each test
>       logging.config.dictConfig({})

pytutils/Test4DT_tests/test_pytutils_log_configure_3_test_valid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/logging/config.py:823: in dictConfig
    dictConfigClass(config).configure()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <logging.config.DictConfigurator object at 0x7f35a5877bd0>

    def configure(self):
        """Do the configuration."""
    
        config = self.config
        if 'version' not in config:
>           raise ValueError("dictionary doesn't specify a version")
E           ValueError: dictionary doesn't specify a version

/usr/local/lib/python3.11/logging/config.py:506: ValueError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-wzfwi05g'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-s1og2324'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-g4tmf3yy'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR ../../../dev/::test_valid_inputs - ValueError: dictionary doesn't speci...
========================= 3 warnings, 1 error in 0.09s =========================
"""