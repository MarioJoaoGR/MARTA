
import pytest
from pytutils.timers import Timer

def test_timer_init():
    timer = Timer(name='test', verbose=True)
    assert timer.name == 'test'
    assert timer.verbose is True

def test_timer_context_manager():
    with pytest.raises(Exception):  # Since we don't have a long operation, any exception will do to ensure the context manager works
        with Timer() as t:
            pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

../../../dev .F                                                          [100%]

=================================== FAILURES ===================================
__________________________ test_timer_context_manager __________________________

    def test_timer_context_manager():
>       with pytest.raises(Exception):  # Since we don't have a long operation, any exception will do to ensure the context manager works
E       Failed: DID NOT RAISE <class 'Exception'>

pytutils/Test4DT_tests/test_pytutils_timers_Timer___init___4_test_edge_cases.py:11: Failed
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-er8s4os9'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-60d6wrf9'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-xqevxf1p'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_timer_context_manager - Failed: DID NOT RAISE <cla...
=================== 1 failed, 1 passed, 3 warnings in 0.07s ====================
"""