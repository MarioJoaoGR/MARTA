
import pytest
from unittest.mock import patch, MagicMock
import sys
import os
import functools
from pytutils.files import islurp

@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_valid_case_chunk_mode():
    with patch('builtins.open', create=True) as mock_file:
        mock_file.return_value.__iter__.side_effect = lambda: iter(['line1\n', 'line2\n', 'line3\n'])

        gen = islurp('example.txt', iter_by=2)
        assert next(gen) == 'li'

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
__________________________ test_valid_case_chunk_mode __________________________

    @pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
    def test_valid_case_chunk_mode():
        with patch('builtins.open', create=True) as mock_file:
            mock_file.return_value.__iter__.side_effect = lambda: iter(['line1\n', 'line2\n', 'line3\n'])
    
            gen = islurp('example.txt', iter_by=2)
>           assert next(gen) == 'li'
E           AssertionError: assert <MagicMock name='open().read()' id='139911679936784'> == 'li'
E            +  where <MagicMock name='open().read()' id='139911679936784'> = next(<generator object islurp at 0x7f3fb9fbc150>)

pytutils/Test4DT_tests/test_pytutils_files_islurp_0_test_valid_case_chunk_mode.py:15: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-nus4becq'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-ta7k6onc'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-z27dhzc3'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_case_chunk_mode - AssertionError: assert <Ma...
======================== 1 failed, 3 warnings in 0.05s =========================
"""