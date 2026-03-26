
import pytest
from pytutils.memo import cachedmethod, _default

def test_valid_inputs():
    def expensive_function(self, arg):
        # Some expensive computation here
        return f"Result for {arg}"

    @cachedmethod(cache=lambda: {}, key=_default, lock=None, typed=_default, cached_exception=Exception)
    def wrapper(self, *args, **kwargs):
        return expensive_function(self, *args, **kwargs)

    # Test with valid inputs
    instance = object()
    arg1 = "arg1"
    arg2 = "arg2"
    
    result1 = wrapper(instance, arg1)
    assert result1 == f"Result for {arg1}"
    
    result2 = wrapper(instance, arg2)
    assert result2 == f"Result for {arg2}"

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

pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        def expensive_function(self, arg):
            # Some expensive computation here
            return f"Result for {arg}"
    
>       @cachedmethod(cache=lambda: {}, key=_default, lock=None, typed=_default, cached_exception=Exception)

pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_valid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

method = <function test_valid_inputs.<locals>.wrapper at 0x7f0a495a3c40>

    def decorator(method):
        # pass method to default key function for backwards compatibilty
        if key is _default:
>           makekey = functools.partial(cachetools.typedkey if typed else cachetools.hashkey, method)
E           AttributeError: module 'cachetools' has no attribute 'hashkey'

pytutils/pytutils/memo.py:39: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.05s ===============================
"""