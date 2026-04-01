
import pytest
from pytutils.memo import cachedmethod
import functools
import warnings
import six

# Mocking cachetools for testing purposes
cachetools = pytest.mark.skip("cachetools is not installed", reason="cachetools is not installed")

def test_cachedmethod():
    @cachedmethod(cache=dict)
    def expensive_calculation(self, a, b):
        return a + b

    # Test the cached method
    assert expensive_calculation(None, 1, 2) == 3
    assert expensive_calculation(None, 1, 2) == 3  # Should be fetched from cache

    @cachedmethod(cache=dict, key=lambda self, *args, **kwargs: (args, kwargs))
    def complex_calculation(self, x, y):
        return x * y

    # Test the cached method with custom key function
    assert complex_calculation(None, 3, 4) == 12
    assert complex_calculation(None, 3, 4) == 12  # Should be fetched from cache

    @cachedmethod(cache=dict, lock=lambda self: None)
    def thread_safe_operation(self):
        pass

    # Test the cached method with locking mechanism (mocked by not doing anything)
    thread_safe_operation(None)  # Should execute without error

    @cachedmethod(cache=dict, cached_exception=ValueError)
    def calculation_with_exception(self, value):
        if value < 0:
            raise ValueError("Value must be non-negative")
        return value * 2

    # Test the cached method with exception handling
    assert calculation_with_exception(None, 5) == 10
    with pytest.raises(ValueError):
        calculation_with_exception(None, -1)  # Should raise an error and be cached
    assert calculation_with_exception(None, -1) is None  # Should fetch from cache

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
______________________________ test_cachedmethod _______________________________

    def test_cachedmethod():
>       @cachedmethod(cache=dict)

pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_1_test_edge_cases.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

method = <function test_cachedmethod.<locals>.expensive_calculation at 0x7f511adae520>

    def decorator(method):
        # pass method to default key function for backwards compatibilty
        if key is _default:
>           makekey = functools.partial(cachetools.typedkey if typed else cachetools.hashkey, method)
E           AttributeError: module 'cachetools' has no attribute 'hashkey'

pytutils/pytutils/memo.py:39: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_1_test_edge_cases.py::test_cachedmethod
============================== 1 failed in 0.08s ===============================
"""