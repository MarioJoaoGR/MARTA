
from pymonet.utils import memoize, eq
from typing import Callable, List, Any

def test_memoize_none():
    def add(x):
        return x + 1
    
    memoized_add = memoize(add)
    
    # First call should compute the result and cache it
    assert memoized_add(None) == 1

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
______________________________ test_memoize_none _______________________________

    def test_memoize_none():
        def add(x):
            return x + 1
    
        memoized_add = memoize(add)
    
        # First call should compute the result and cache it
>       assert memoized_add(None) == 1

pyMonet/Test4DT_tests/test_pymonet_utils_memoize_1_test_edge_case_none.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/utils.py:160: in memoized_fn
    fn_result = fn(argument)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = None

    def add(x):
>       return x + 1
E       TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

pyMonet/Test4DT_tests/test_pymonet_utils_memoize_1_test_edge_case_none.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_memoize_1_test_edge_case_none.py::test_memoize_none
============================== 1 failed in 0.06s ===============================
"""