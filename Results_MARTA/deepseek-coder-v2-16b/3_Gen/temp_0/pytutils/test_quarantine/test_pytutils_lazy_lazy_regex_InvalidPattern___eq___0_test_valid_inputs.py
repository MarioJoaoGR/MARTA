
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_valid_inputs():
    # Test initialization with a valid message
    msg = "Invalid character found in pattern."
    invalid_pattern = InvalidPattern(msg)
    assert invalid_pattern.msg == msg
    
    # Test equality method
    other_invalid_pattern = InvalidPattern(msg)
    assert invalid_pattern == other_invalid_pattern
    
    # Test inequality due to different classes
    class OtherClass:
        pass
    
    other_object = OtherClass()
    with pytest.raises(NotImplementedError):
        assert invalid_pattern.__eq__(other_object)

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
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test initialization with a valid message
        msg = "Invalid character found in pattern."
        invalid_pattern = InvalidPattern(msg)
        assert invalid_pattern.msg == msg
    
        # Test equality method
        other_invalid_pattern = InvalidPattern(msg)
        assert invalid_pattern == other_invalid_pattern
    
        # Test inequality due to different classes
        class OtherClass:
            pass
    
        other_object = OtherClass()
>       with pytest.raises(NotImplementedError):
E       Failed: DID NOT RAISE <class 'NotImplementedError'>

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_InvalidPattern___eq___0_test_valid_inputs.py:20: Failed
=============================== warnings summary ===============================
::test_valid_inputs
  /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_InvalidPattern___eq___0_test_valid_inputs.py:21: DeprecationWarning: NotImplemented should not be used in a boolean context
    assert invalid_pattern.__eq__(other_object)

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-us4b39kc'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-2533lnxs'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-flwesk3s'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_inputs - Failed: DID NOT RAISE <class 'NotIm...
======================== 1 failed, 4 warnings in 0.06s =========================
"""