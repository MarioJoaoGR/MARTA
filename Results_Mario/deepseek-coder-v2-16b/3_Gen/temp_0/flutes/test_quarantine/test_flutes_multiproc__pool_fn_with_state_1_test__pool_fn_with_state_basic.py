
import pytest
from flutes.multiproc import _pool_fn_with_state

def test__pool_fn_with_state_basic():
    def compute_function(state, *args):
        # Use the state and args to perform some computation
        result = sum(args) + state['value']
        return result
    
    state = {'value': 10}
    computed_result = _pool_fn_with_state(compute_function, *(1, 2, 3), **{'__state__': state})
    assert computed_result == 16  # Expected result is 1 + 2 + 3 + 10

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_1_test__pool_fn_with_state_basic.py F [100%]

=================================== FAILURES ===================================
________________________ test__pool_fn_with_state_basic ________________________

    def test__pool_fn_with_state_basic():
        def compute_function(state, *args):
            # Use the state and args to perform some computation
            result = sum(args) + state['value']
            return result
    
        state = {'value': 10}
>       computed_result = _pool_fn_with_state(compute_function, *(1, 2, 3), **{'__state__': state})

flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_1_test__pool_fn_with_state_basic.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

fn = <function test__pool_fn_with_state_basic.<locals>.compute_function at 0x7f478a6919e0>
args = (1, 2, 3), kwds = {'__state__': {'value': 10}}, frame = None

    def _pool_fn_with_state(fn: Callable[..., R], *args, **kwds) -> R:
        # Wrapper for compute function passed to stateful pools.
        frame = cast(FrameType, inspect.currentframe().f_back)  # type: ignore[union-attr]
>       while '__state__' not in frame.f_locals:  # the function might be wrapped several types
E       AttributeError: 'NoneType' object has no attribute 'f_locals'

flutes/flutes/multiproc.py:194: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_1_test__pool_fn_with_state_basic.py::test__pool_fn_with_state_basic
============================== 1 failed in 0.10s ===============================

"""