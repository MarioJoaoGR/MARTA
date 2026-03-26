
import pytest
from typing import List, Callable, Tuple, Any, Dict

# Assuming _chain_fns is defined in a module named 'flutes.multiproc'
from flutes.multiproc import _chain_fns

def test_invalid_inputs():
    # Define some dummy functions and arguments for testing
    def add(a, b):
        return a + b
    
    def multiply(a, b, c=1):
        return a * b * c
    
    fns = [add, multiply]
    fn_arg_kwargs = [( (1, 2), {} ), ( (3, 4), {'c': 5} )]
    
    # Test with invalid inputs: non-matching lengths of fns and fn_arg_kwargs
    with pytest.raises(IndexError):
        _chain_fns([add], fn_arg_kwargs)
        
    # Test with invalid inputs: empty list for functions
    with pytest.raises(ValueError):
        _chain_fns([], fn_arg_kwargs)
    
    # Test with invalid inputs: non-matching lengths of arguments and keyword arguments
    with pytest.raises(IndexError):
        _chain_fns(fns, [( (1, 2), {})])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Define some dummy functions and arguments for testing
        def add(a, b):
            return a + b
    
        def multiply(a, b, c=1):
            return a * b * c
    
        fns = [add, multiply]
        fn_arg_kwargs = [( (1, 2), {} ), ( (3, 4), {'c': 5} )]
    
        # Test with invalid inputs: non-matching lengths of fns and fn_arg_kwargs
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_2_test_invalid_inputs.py:20: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.12s ===============================
"""