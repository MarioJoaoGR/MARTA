
import pytest
from flutes.multiproc import FuncWrapper

def add(a, b):
    return a + b

wrapper = FuncWrapper(add, (1, 2), {'b': 3})

def test_valid_inputs():
    result = wrapper()
    assert result == 4

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
>       result = wrapper()

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___0_test_valid_inputs.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.FuncWrapper object at 0x7f3fea7d3f50>, args = ()

    def __call__(self, *args):
>       return self.fn(*args, *self.args, **self.kwds)
E       TypeError: add() got multiple values for argument 'b'

flutes/flutes/multiproc.py:219: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.09s ===============================
"""