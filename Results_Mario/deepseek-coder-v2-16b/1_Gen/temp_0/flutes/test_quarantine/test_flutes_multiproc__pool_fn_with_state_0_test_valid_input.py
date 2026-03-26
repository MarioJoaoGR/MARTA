
import pytest
from flutes.multiproc import _pool_fn_with_state

def test_valid_input():
    def compute_function(state, *args):
        return sum(args) + state['value']
    
    state = {'value': 10}
    
    # Call the function with valid arguments
    result = _pool_fn_with_state(compute_function, *(1, 2, 3), **{'__state__': state})
    
    assert result == 16

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

flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        def compute_function(state, *args):
            return sum(args) + state['value']
    
        state = {'value': 10}
    
        # Call the function with valid arguments
>       result = _pool_fn_with_state(compute_function, *(1, 2, 3), **{'__state__': state})

flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_0_test_valid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

fn = <function test_valid_input.<locals>.compute_function at 0x7fc44b716b60>
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
FAILED flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""