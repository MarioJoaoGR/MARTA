
# Module: flutes.multiproc
import pytest
from typing import List, Callable, Tuple, Dict, Any

# Define some example functions
def add(a, b):
    return a + b

def multiply(a, b, c=1):
    return a * b * c

# Example list of callables and their arguments/kwargs
fns = [add, multiply]
fn_arg_kwargs = [( (1, 2), {} ), ( (3, 4), {'c': 5} )]

def test__chain_fns():
    # Call the function with the example data
    results = _chain_fns(fns, fn_arg_kwargs)
    assert results == [3, 60], f"Expected [3, 60] but got {results}"

def test__chain_fns_with_empty_lists():
    # Test with empty lists for both functions and arguments/kwargs
    empty_results = _chain_fns([], [])
    assert empty_results == [], f"Expected [] but got {empty_results}"

def test__chain_fns_with_one_function():
    # Test with only one function in the list of functions
    single_fn_list = [add]
    single_arg_kwargs = [( (1, 2), {} )]
    single_result = _chain_fns(single_fn_list, single_arg_kwargs)
    assert single_result == [3], f"Expected [3] but got {single_result}"

def test__chain_fns_with_one_argument():
    # Test with only one set of arguments/kwargs for all functions
    one_set_of_args = [( (1, 2), {} ), ( (1, 2), {} )]
    result_with_one_set = _chain_fns(fns, one_set_of_args)
    assert result_with_one_set == [3, 3], f"Expected [3, 3] but got {result_with_one_set}"

def test__chain_fns_with_incorrect_types():
    # Test with incorrect types for functions and arguments/kwargs
    with pytest.raises(TypeError):
        _chain_fns("not a list", "not the correct type")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__chain_fns_0
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0.py:19:14: E0602: Undefined variable '_chain_fns' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0.py:24:20: E0602: Undefined variable '_chain_fns' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0.py:31:20: E0602: Undefined variable '_chain_fns' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0.py:37:26: E0602: Undefined variable '_chain_fns' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0.py:43:8: E0602: Undefined variable '_chain_fns' (undefined-variable)


"""