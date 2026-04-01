
import pytest
from flutes.multiproc import FuncWrapper

def my_function(a, b, key=None):
    return a + b + (key or 0)

def test_valid_inputs():
    func_wrapper = FuncWrapper(my_function, (1, 2), {'key': 'value'})
    
    # Call the function with additional positional and keyword arguments
    result = func_wrapper(3, c=4)
    
    assert result == my_function(1, 2, key='value') + 3

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        func_wrapper = FuncWrapper(my_function, (1, 2), {'key': 'value'})
    
        # Call the function with additional positional and keyword arguments
>       result = func_wrapper(3, c=4)
E       TypeError: FuncWrapper.__call__() got an unexpected keyword argument 'c'

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___0_test_valid_inputs.py:12: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.09s ===============================
"""