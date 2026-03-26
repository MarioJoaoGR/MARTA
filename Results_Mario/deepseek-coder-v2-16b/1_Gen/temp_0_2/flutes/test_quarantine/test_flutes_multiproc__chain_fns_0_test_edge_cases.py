
import pytest
from flutes.multiproc import _chain_fns

def test_edge_cases():
    fns = [None, lambda x, y: x + y]
    fn_arg_kwargs = [((), {}), ((1,), {'y': 3})]
    
    # Test with None functions
    result = _chain_fns(fns, fn_arg_kwargs)
    
    assert result == [None, 4]

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

flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        fns = [None, lambda x, y: x + y]
        fn_arg_kwargs = [((), {}), ((1,), {'y': 3})]
    
        # Test with None functions
>       result = _chain_fns(fns, fn_arg_kwargs)

flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_edge_cases.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

fns = [None, <function test_edge_cases.<locals>.<lambda> at 0x7f16f62c68e0>]
fn_arg_kwargs = [((), {}), ((1,), {'y': 3})]

    def _chain_fns(fns: List[Callable[..., R]], fn_arg_kwargs: List[Tuple[Tuple[Any, ...], Dict[str, Any]]]) -> List[R]:
        rets = []
        for fn, (args, kwargs) in zip(fns, fn_arg_kwargs):
>           rets.append(fn(*args, **kwargs))
E           TypeError: 'NoneType' object is not callable

flutes/flutes/multiproc.py:205: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.10s ===============================
"""