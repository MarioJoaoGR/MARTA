
import pytest
from flutes.multiproc import _chain_fns

def test_chain_fns_edge_cases():
    # Test with None input
    fns = [lambda x: x]
    fn_arg_kwargs = [(None, {})]
    assert _chain_fns(fns, fn_arg_kwargs) == [None]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
__________________________ test_chain_fns_edge_cases ___________________________

    def test_chain_fns_edge_cases():
        # Test with None input
        fns = [lambda x: x]
        fn_arg_kwargs = [(None, {})]
>       assert _chain_fns(fns, fn_arg_kwargs) == [None]

flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_edge_cases.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

fns = [<function test_chain_fns_edge_cases.<locals>.<lambda> at 0x7fce9dfc8d60>]
fn_arg_kwargs = [(None, {})]

    def _chain_fns(fns: List[Callable[..., R]], fn_arg_kwargs: List[Tuple[Tuple[Any, ...], Dict[str, Any]]]) -> List[R]:
        rets = []
        for fn, (args, kwargs) in zip(fns, fn_arg_kwargs):
>           rets.append(fn(*args, **kwargs))
E           TypeError: Test4DT_tests.test_flutes_multiproc__chain_fns_0_test_edge_cases.test_chain_fns_edge_cases.<locals>.<lambda>() argument after * must be an iterable, not NoneType

flutes/flutes/multiproc.py:205: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_edge_cases.py::test_chain_fns_edge_cases
============================== 1 failed in 0.08s ===============================

"""