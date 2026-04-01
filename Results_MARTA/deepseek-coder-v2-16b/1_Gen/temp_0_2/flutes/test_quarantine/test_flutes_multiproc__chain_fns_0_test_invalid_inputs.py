
from typing import List, Callable, Tuple, Any, Dict
import pytest
from flutes.multiproc import _chain_fns

def test_invalid_inputs():
    # Test when fns is empty
    with pytest.raises(IndexError):
        _chain_fns([], [((), {})])

    # Test when fn_arg_kwargs is empty
    assert _chain_fns([lambda x: x], []) == []

    # Test when lengths of fns and fn_arg_kwargs do not match
    with pytest.raises(IndexError):
        _chain_fns([lambda x: x, lambda y: y], [((), {})])

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

flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test when fns is empty
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_invalid_inputs.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.10s ===============================
"""