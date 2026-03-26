
import pytest
from pytutils.urls import update_query_params

def test_valid_input():
    # Test case with valid URL and parameters
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    expected_output = 'http://example.com?...foo=stuff...'
    
    assert update_query_params(url, params) == expected_output

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
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test case with valid URL and parameters
        url = 'http://example.com?foo=bar&biz=baz'
        params = {'foo': 'stuff'}
        expected_output = 'http://example.com?...foo=stuff...'
    
>       assert update_query_params(url, params) == expected_output
E       AssertionError: assert 'http://examp...stuff&biz=baz' == 'http://examp....foo=stuff...'
E         
E         - http://example.com?...foo=stuff...
E         ?                    ---         ^^^
E         + http://example.com?foo=stuff&biz=baz
E         ?                             ^^^^^^^^

pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py:11: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-ms4xk8zv'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-166ru6q1'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-zp9u6fj_'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_input - AssertionError: assert 'http://examp...
======================== 1 failed, 3 warnings in 0.05s =========================
"""