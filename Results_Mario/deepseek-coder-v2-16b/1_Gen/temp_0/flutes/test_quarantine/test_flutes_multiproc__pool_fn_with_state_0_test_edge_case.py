
import pytest
from flutes.multiproc import _pool_fn_with_state

def test_edge_case():
    # Define a dummy compute function that will be passed to _pool_fn_with_state
    def compute_function(state: dict, *args: int) -> int:
        return sum(args) + state['value']
    
    # Create an empty state object
    state = {}
    
    # Call the function with None as the compute function and an empty state object
    result = _pool_fn_with_state(None, *range(10), __state__=state)
    
    assert result is None, "Expected result to be None since fn is None"

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

flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Define a dummy compute function that will be passed to _pool_fn_with_state
        def compute_function(state: dict, *args: int) -> int:
            return sum(args) + state['value']
    
        # Create an empty state object
        state = {}
    
        # Call the function with None as the compute function and an empty state object
>       result = _pool_fn_with_state(None, *range(10), __state__=state)

flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_0_test_edge_case.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

fn = None, args = (0, 1, 2, 3, 4, 5, ...), kwds = {'__state__': {}}
frame = None

    def _pool_fn_with_state(fn: Callable[..., R], *args, **kwds) -> R:
        # Wrapper for compute function passed to stateful pools.
        frame = cast(FrameType, inspect.currentframe().f_back)  # type: ignore[union-attr]
>       while '__state__' not in frame.f_locals:  # the function might be wrapped several types
E       AttributeError: 'NoneType' object has no attribute 'f_locals'

flutes/flutes/multiproc.py:194: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.11s ===============================
"""