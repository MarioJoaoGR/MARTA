
import inspect
from typing import Callable, TypeVar, cast
from types import FrameType
from flutes.multiproc import _pool_fn_with_state

R = TypeVar('R')

def test_edge_case():
    def compute_function(state, data):
        assert state is None
        assert data == []
        return "result"
    
    result = _pool_fn_with_state(compute_function)
    assert result == "result"

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

flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        def compute_function(state, data):
            assert state is None
            assert data == []
            return "result"
    
>       result = _pool_fn_with_state(compute_function)

flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_1_test_edge_case.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

fn = <function test_edge_case.<locals>.compute_function at 0x7f74f85e60c0>
args = (), kwds = {}, frame = None

    def _pool_fn_with_state(fn: Callable[..., R], *args, **kwds) -> R:
        # Wrapper for compute function passed to stateful pools.
        frame = cast(FrameType, inspect.currentframe().f_back)  # type: ignore[union-attr]
>       while '__state__' not in frame.f_locals:  # the function might be wrapped several types
E       AttributeError: 'NoneType' object has no attribute 'f_locals'

flutes/flutes/multiproc.py:194: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.10s ===============================
"""