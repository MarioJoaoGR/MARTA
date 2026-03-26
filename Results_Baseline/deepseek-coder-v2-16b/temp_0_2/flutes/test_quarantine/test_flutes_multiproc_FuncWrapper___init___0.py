
# Module: flutes.multiproc
# Import the function from its module
from flutes.multiproc import FuncWrapper

import pytest

# Test cases for FuncWrapper class
def test_func_wrapper_basic():
    def example_function(a, b=2):
        return a + b
    
    func_wrapper = FuncWrapper(example_function, (1,), {'b': 3})
    result = func_wrapper()
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___0.py .F  [100%]

=================================== FAILURES ===================================
_______________________ test_func_wrapper_additional_arg _______________________

    def test_func_wrapper_additional_arg():
        def example_function(a, b=2):
            return a + b
    
        func_wrapper = FuncWrapper(example_function, (1,), {'b': 3})
>       result = func_wrapper(2)  # Corrected to pass only one argument

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___0.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.FuncWrapper object at 0x7fec0a740950>, args = (2,)

    def __call__(self, *args):
>       return self.fn(*args, *self.args, **self.kwds)
E       TypeError: test_func_wrapper_additional_arg.<locals>.example_function() got multiple values for argument 'b'

flutes/flutes/multiproc.py:219: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___0.py::test_func_wrapper_additional_arg
========================= 1 failed, 1 passed in 0.10s ==========================
"""