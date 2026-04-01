
import pytest
from flutes.multiproc import _pool_fn_with_state

def test_invalid_inputs():
    # Test case 1: fn is not callable
    with pytest.raises(TypeError) as excinfo:
        _pool_fn_with_state("not a callable")  # type: ignore
    assert "expected Callable" in str(excinfo.value)

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

flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test case 1: fn is not callable
        with pytest.raises(TypeError) as excinfo:
>           _pool_fn_with_state("not a callable")  # type: ignore

flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_0_test_invalid_inputs.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

fn = 'not a callable', args = (), kwds = {}, frame = None

    def _pool_fn_with_state(fn: Callable[..., R], *args, **kwds) -> R:
        # Wrapper for compute function passed to stateful pools.
        frame = cast(FrameType, inspect.currentframe().f_back)  # type: ignore[union-attr]
>       while '__state__' not in frame.f_locals:  # the function might be wrapped several types
E       AttributeError: 'NoneType' object has no attribute 'f_locals'

flutes/flutes/multiproc.py:194: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.12s ===============================
"""