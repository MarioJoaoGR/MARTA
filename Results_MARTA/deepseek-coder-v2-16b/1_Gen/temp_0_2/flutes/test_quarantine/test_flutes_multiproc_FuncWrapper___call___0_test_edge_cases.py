
import pytest
from flutes.multiproc import FuncWrapper

def my_function(a, b, key=None):
    return a + b + (0 if key is None else int(key))

def test_edge_cases():
    func_wrapper = FuncWrapper(my_function, (1, 2), {'key': 'value'})
    
    # Test with None values
    assert func_wrapper(None, None) == 3

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

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        func_wrapper = FuncWrapper(my_function, (1, 2), {'key': 'value'})
    
        # Test with None values
>       assert func_wrapper(None, None) == 3

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___0_test_edge_cases.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.FuncWrapper object at 0x7f11528bec50>
args = (None, None)

    def __call__(self, *args):
>       return self.fn(*args, *self.args, **self.kwds)
E       TypeError: my_function() got multiple values for argument 'key'

flutes/flutes/multiproc.py:219: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.10s ===============================
"""