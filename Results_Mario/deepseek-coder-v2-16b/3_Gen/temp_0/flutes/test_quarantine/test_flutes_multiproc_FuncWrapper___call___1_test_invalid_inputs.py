
import pytest
from typing import Callable, Iterable, Mapping, Any
from flutes.multiproc import FuncWrapper

def example_function(a, b=None):
    return a + (b or 0)

@pytest.fixture
def func_wrapper():
    fn = example_function
    args = (1,)
    kwds = {'b': 2}
    return FuncWrapper(fn, args, kwds)

def test_invalid_inputs(func_wrapper):
    with pytest.raises(TypeError):
        func_wrapper()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

func_wrapper = <flutes.multiproc.FuncWrapper object at 0x7f64d38f1050>

    def test_invalid_inputs(func_wrapper):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___1_test_invalid_inputs.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.07s ===============================

"""