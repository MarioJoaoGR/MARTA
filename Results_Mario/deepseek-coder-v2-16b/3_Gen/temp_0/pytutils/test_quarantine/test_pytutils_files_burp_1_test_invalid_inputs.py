
import pytest
from pytutils.files import burp
import sys
import os

def test_invalid_inputs():
    # Test invalid filename type (should raise TypeError)
    with pytest.raises(TypeError):
        burp(42, "contents")  # filename is an integer, not a string
    
    # Test invalid mode type (should raise TypeError)
    with pytest.raises(TypeError):
        burp("filename", "contents", mode=42)  # mode is an integer, not a string
    
    # Test invalid allow_stdout type (should raise TypeError)
    with pytest.raises(TypeError):
        burp("filename", "contents", allow_stdout=42)  # allow_stdout is not a boolean

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
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test invalid filename type (should raise TypeError)
        with pytest.raises(TypeError):
            burp(42, "contents")  # filename is an integer, not a string
    
        # Test invalid mode type (should raise TypeError)
        with pytest.raises(TypeError):
            burp("filename", "contents", mode=42)  # mode is an integer, not a string
    
        # Test invalid allow_stdout type (should raise TypeError)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_files_burp_1_test_invalid_inputs.py:17: Failed
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-rq2gakys'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-nzsrlmn_'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-przud4q4'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_invalid_inputs - Failed: DID NOT RAISE <class 'Typ...
======================== 1 failed, 3 warnings in 0.08s =========================
"""