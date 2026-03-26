
import pytest
from typing import List, Callable, Tuple, Dict, Any, TypeVar

R = TypeVar('R')

# Import the function from its module
from flutes.multiproc import _chain_fns

def test_basic_usage():
    def add(a, b):
        return a + b
    
    def multiply(a, b):
        return a * b
    
    fns = [add, multiply]
    fn_arg_kwargs = [( (1, 2), {} ), ( (3, 4), {'b': 5} )]
    result = _chain_fns(fns, fn_arg_kwargs)
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

flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0.py F             [100%]

=================================== FAILURES ===================================
_______________________________ test_basic_usage _______________________________

    def test_basic_usage():
        def add(a, b):
            return a + b
    
        def multiply(a, b):
            return a * b
    
        fns = [add, multiply]
        fn_arg_kwargs = [( (1, 2), {} ), ( (3, 4), {'b': 5} )]
>       result = _chain_fns(fns, fn_arg_kwargs)

flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

fns = [<function test_basic_usage.<locals>.add at 0x7faac7f1fec0>, <function test_basic_usage.<locals>.multiply at 0x7faac7f1fc40>]
fn_arg_kwargs = [((1, 2), {}), ((3, 4), {'b': 5})]

    def _chain_fns(fns: List[Callable[..., R]], fn_arg_kwargs: List[Tuple[Tuple[Any, ...], Dict[str, Any]]]) -> List[R]:
        rets = []
        for fn, (args, kwargs) in zip(fns, fn_arg_kwargs):
>           rets.append(fn(*args, **kwargs))
E           TypeError: test_basic_usage.<locals>.multiply() got multiple values for argument 'b'

flutes/flutes/multiproc.py:205: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0.py::test_basic_usage
============================== 1 failed in 0.11s ===============================
"""