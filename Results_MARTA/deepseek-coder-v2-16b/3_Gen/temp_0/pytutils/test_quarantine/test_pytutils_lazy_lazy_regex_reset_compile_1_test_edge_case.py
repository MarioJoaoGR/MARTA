
import pytest
from unittest.mock import patch
import pytutils.lazy.lazy_regex as lazy_regex

def test_reset_compile():
    # Mock the original re.compile function
    with patch('pytutils.lazy.lazy_regex.re.compile', autospec=True) as mock_compile:
        _real_re_compile = lazy_regex.re.compile  # Save the original compile function
        
        # Call reset_compile to ensure it restores re.compile to its initial state
        lazy_regex.reset_compile()
        
        # Assert that re.compile has been restored to its original implementation
        mock_compile.assert_called_once_with()

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
______________________________ test_reset_compile ______________________________

    def test_reset_compile():
        # Mock the original re.compile function
        with patch('pytutils.lazy.lazy_regex.re.compile', autospec=True) as mock_compile:
            _real_re_compile = lazy_regex.re.compile  # Save the original compile function
    
            # Call reset_compile to ensure it restores re.compile to its initial state
            lazy_regex.reset_compile()
    
            # Assert that re.compile has been restored to its original implementation
>           mock_compile.assert_called_once_with()

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_reset_compile_1_test_edge_case.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:220: in assert_called_once_with
    return mock.assert_called_once_with(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='compile' spec='function' id='139778303057936'>
args = (), kwargs = {}
msg = "Expected 'compile' to be called once. Called 0 times."

    def assert_called_once_with(self, /, *args, **kwargs):
        """assert that the mock was called exactly once and that that call was
        with the specified arguments."""
        if not self.call_count == 1:
            msg = ("Expected '%s' to be called once. Called %s times.%s"
                   % (self._mock_name or 'mock',
                      self.call_count,
                      self._calls_repr()))
>           raise AssertionError(msg)
E           AssertionError: Expected 'compile' to be called once. Called 0 times.

/usr/local/lib/python3.11/unittest/mock.py:950: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-x2hwoe82'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-ufer_a5o'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-l6up84bw'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_reset_compile - AssertionError: Expected 'compile'...
======================== 1 failed, 3 warnings in 0.09s =========================
"""