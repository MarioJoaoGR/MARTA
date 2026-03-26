
import pytest
from pytutils.pythree import ensure_encoded_bytes

def test_invalid_inputs():
    # Test with invalid inputs and expected exceptions
    with pytest.raises(TypeError):
        ensure_encoded_bytes(12345)  # int is not allowed

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
        # Test with invalid inputs and expected exceptions
        with pytest.raises(TypeError):
>           ensure_encoded_bytes(12345)  # int is not allowed

pytutils/Test4DT_tests/test_pytutils_pythree_ensure_encoded_bytes_3_test_invalid_inputs.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = 12345, encoding = 'utf-8', errors = 'strict'
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
E           AttributeError: 'int' object has no attribute 'encode'

pytutils/pytutils/pythree.py:16: AttributeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-tip3vd5p'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-k0c8x8a3'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-iq65v1yk'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_invalid_inputs - AttributeError: 'int' object has ...
======================== 1 failed, 3 warnings in 0.07s =========================
"""