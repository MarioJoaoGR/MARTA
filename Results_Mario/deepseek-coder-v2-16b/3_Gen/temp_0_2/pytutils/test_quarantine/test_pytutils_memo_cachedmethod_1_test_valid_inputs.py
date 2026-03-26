
import pytest
from pytutils.memo import cachedmethod, _default, CachedException
import functools
import warnings
import six

def test_cachedmethod_valid_inputs():
    @cachedmethod(cache=dict)
    def expensive_calculation(self, a, b):
        return a + b

    # Test with default key function and no lock
    assert expensive_calculation(None, 2, 3) == 5
    assert expensive_calculation(None, 2, 3) == 5  # Second call should be cached

if __name__ == "__main__":
    pytest.main()

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

pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
________________________ test_cachedmethod_valid_inputs ________________________

    def test_cachedmethod_valid_inputs():
>       @cachedmethod(cache=dict)

pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_1_test_valid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

method = <function test_cachedmethod_valid_inputs.<locals>.expensive_calculation at 0x7f4438434900>

    def decorator(method):
        # pass method to default key function for backwards compatibilty
        if key is _default:
>           makekey = functools.partial(cachetools.typedkey if typed else cachetools.hashkey, method)
E           AttributeError: module 'cachetools' has no attribute 'hashkey'

pytutils/pytutils/memo.py:39: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_1_test_valid_inputs.py::test_cachedmethod_valid_inputs
============================== 1 failed in 0.09s ===============================
"""