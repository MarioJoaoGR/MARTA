
import pytest
from pytutils.memo import lazyproperty

class InvalidInputClass:
    pass  # This class is used to simulate an object with no 'valid' member.

def test_invalid_inputs():
    """Test that the lazyproperty decorator raises a meaningful error when applied to an invalid input."""
    
    # Define a function that will be decorated by lazyproperty
    def expensive_calculation(self):
        return sum(i**2 for i in range(1000))

    # Apply the lazyproperty decorator to the function
    @lazyproperty
    def lp_expensive_calculation(self):
        return sum(i**2 for i in range(1000))

    # Create an instance of a class with no 'valid' member
    invalid_instance = InvalidInputClass()

    # Test that applying the lazyproperty decorator to an invalid input raises a meaningful error
    with pytest.raises(AttributeError) as excinfo:
        lp_expensive_calculation(invalid_instance)
    
    assert str(excinfo.value) == "InvalidInputClass instance has no attribute '_lazy__expensive_calculation'"

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
        """Test that the lazyproperty decorator raises a meaningful error when applied to an invalid input."""
    
        # Define a function that will be decorated by lazyproperty
        def expensive_calculation(self):
            return sum(i**2 for i in range(1000))
    
        # Apply the lazyproperty decorator to the function
        @lazyproperty
        def lp_expensive_calculation(self):
            return sum(i**2 for i in range(1000))
    
        # Create an instance of a class with no 'valid' member
        invalid_instance = InvalidInputClass()
    
        # Test that applying the lazyproperty decorator to an invalid input raises a meaningful error
        with pytest.raises(AttributeError) as excinfo:
>           lp_expensive_calculation(invalid_instance)
E           TypeError: 'property' object is not callable

pytutils/Test4DT_tests/test_pytutils_memo_lazyproperty_5_test_invalid_inputs.py:25: TypeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-4t2zdz_9'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-5lsb59qt'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-3vc2545g'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_invalid_inputs - TypeError: 'property' object is n...
======================== 1 failed, 3 warnings in 0.08s =========================
"""