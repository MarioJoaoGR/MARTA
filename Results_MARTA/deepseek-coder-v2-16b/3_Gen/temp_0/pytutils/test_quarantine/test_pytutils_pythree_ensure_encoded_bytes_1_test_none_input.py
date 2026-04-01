
import pytest
from pytutils.pythree import ensure_encoded_bytes

def test_none_input():
    # Test when input is None
    result = ensure_encoded_bytes(None)
    assert result is None, "Expected None but got a bytes object"

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
_______________________________ test_none_input ________________________________

    def test_none_input():
        # Test when input is None
>       result = ensure_encoded_bytes(None)

pytutils/Test4DT_tests/test_pytutils_pythree_ensure_encoded_bytes_1_test_none_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = None, encoding = 'utf-8', errors = 'strict'
allowed_types = (<class 'bytes'>, <class 'bytearray'>, <class 'memoryview'>)

    def ensure_encoded_bytes(s, encoding='utf-8', errors='strict', allowed_types=(bytes, bytearray, memoryview)):
        """
        Ensure string is encoded as byteslike; convert using specified parameters if we have to.
    
        :param str|bytes|bytesarray|memoryview s: string/byteslike
        :param str encoding: Decode using this encoding
        :param str errors: How to handle errors
        :return bytes|bytesarray|memoryview: Encoded string as str
        """
        if isinstance(s, allowed_types):
            return s
        else:
>           return s.encode(encoding=encoding, errors=errors)
E           AttributeError: 'NoneType' object has no attribute 'encode'

pytutils/pytutils/pythree.py:16: AttributeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-lyeo4l1i'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-yepizffz'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-0dpy76g4'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_none_input - AttributeError: 'NoneType' object has...
======================== 1 failed, 3 warnings in 0.05s =========================
"""