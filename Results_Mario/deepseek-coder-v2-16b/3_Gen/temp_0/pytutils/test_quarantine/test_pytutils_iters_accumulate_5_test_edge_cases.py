
import pytest
from pytutils.iters import accumulate
import operator

def test_edge_cases():
    # Test with empty list
    assert list(accumulate([])) == []
    
    # Test with None input
    with pytest.raises(TypeError):
        list(accumulate(None))
    
    # Test with a single element list
    assert list(accumulate([1])) == [1]
    
    # Test with a list of positive numbers
    assert list(accumulate([1, 2, 3, 4, 5])) == [1, 3, 6, 10, 15]
    
    # Test with a list of negative numbers
    assert list(accumulate([-1, -2, -3, -4, -5])) == [-1, -3, -6, -10, -15]
    
    # Test with a list of mixed positive and negative numbers
    assert list(accumulate([1, -2, 3, -4, 5])) == [1, -1, 2, -2, 3]
    
    # Test with a list of strings (should raise TypeError)
    with pytest.raises(TypeError):
        list(accumulate(["a", "b", "c"]))

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
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test with empty list
        assert list(accumulate([])) == []
    
        # Test with None input
        with pytest.raises(TypeError):
            list(accumulate(None))
    
        # Test with a single element list
        assert list(accumulate([1])) == [1]
    
        # Test with a list of positive numbers
        assert list(accumulate([1, 2, 3, 4, 5])) == [1, 3, 6, 10, 15]
    
        # Test with a list of negative numbers
        assert list(accumulate([-1, -2, -3, -4, -5])) == [-1, -3, -6, -10, -15]
    
        # Test with a list of mixed positive and negative numbers
        assert list(accumulate([1, -2, 3, -4, 5])) == [1, -1, 2, -2, 3]
    
        # Test with a list of strings (should raise TypeError)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_iters_accumulate_5_test_edge_cases.py:27: Failed
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-wrtnj8vk'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-jnv2ivjg'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-k148s5il'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_edge_cases - Failed: DID NOT RAISE <class 'TypeErr...
======================== 1 failed, 3 warnings in 0.08s =========================
"""