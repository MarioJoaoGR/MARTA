
import pytest
from typing import List, Callable, Tuple, Any, Dict, TypeVar

R = TypeVar('R')

def _chain_fns(fns: List[Callable[..., R]], fn_arg_kwargs: List[Tuple[Tuple[Any, ...], Dict[str, Any]]]) -> List[R]:
    rets = []
    for fn, (args, kwargs) in zip(fns, fn_arg_kwargs):
        rets.append(fn(*args, **kwargs))
    return rets

def test_valid_inputs():
    def add(a, b):
        return a + b
    
    def multiply(a, b, c=1):
        return a * b * c
    
    fns = [add, multiply]
    fn_arg_kwargs = [( (1, 2), {} ), ( (3, 4), {'c': 5} )]
    
    results = _chain_fns(fns, fn_arg_kwargs)
    assert results == [3, 15]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        def add(a, b):
            return a + b
    
        def multiply(a, b, c=1):
            return a * b * c
    
        fns = [add, multiply]
        fn_arg_kwargs = [( (1, 2), {} ), ( (3, 4), {'c': 5} )]
    
        results = _chain_fns(fns, fn_arg_kwargs)
>       assert results == [3, 15]
E       assert [3, 60] == [3, 15]
E         
E         At index 1 diff: 60 != 15
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_valid_inputs.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.08s ===============================

"""