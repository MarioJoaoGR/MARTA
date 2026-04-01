
import pytest
from pymonet.utils import memoize

def find(lst, key):
    for item in lst:
        if key(item):
            return item
    return None

@pytest.fixture
def memoized_fn():
    def slow_function(x):
        # Imagine this is a computation-heavy function
        return x * 2
    
    memoized_slow_function = memoize(slow_function, key=lambda x, y: x == y)
    return memoized_slow_function

def test_edge_case_none(memoized_fn):
    # First call will compute the result
    assert memoized_fn(5) == 10
    
    # Second call with the same argument uses the cached result
    assert memoized_fn(5) == 10
    
    # Check that the cache has been updated correctly
    assert len(memoized_fn.cache) == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_utils_memoize_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

memoized_fn = <function memoize.<locals>.memoized_fn at 0x7f6d773c6fc0>

    def test_edge_case_none(memoized_fn):
        # First call will compute the result
        assert memoized_fn(5) == 10
    
        # Second call with the same argument uses the cached result
        assert memoized_fn(5) == 10
    
        # Check that the cache has been updated correctly
>       assert len(memoized_fn.cache) == 1
E       AttributeError: 'function' object has no attribute 'cache'

pyMonet/Test4DT_tests/test_pymonet_utils_memoize_1_test_edge_case_none.py:28: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_memoize_1_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.08s ===============================
"""