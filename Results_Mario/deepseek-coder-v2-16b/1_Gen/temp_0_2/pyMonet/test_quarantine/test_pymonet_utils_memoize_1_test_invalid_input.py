
import pytest
from typing import Callable, List, Any
from pymonent.utils import memoize, eq

def find(lst, predicate):
    for item in lst:
        if predicate(item):
            return item
    return None

@pytest.mark.parametrize("input_type", [int, str, list, dict, tuple])
def test_invalid_input(input_type):
    def add(x):
        return x + 1
    
    memoized_add = memoize(add)
    
    with pytest.raises(TypeError):
        if input_type == int:
            memoized_add(1)
        elif input_type == str:
            memoized_add("string")
        elif input_type == list:
            memoized_add([1, 2, 3])
        elif input_type == dict:
            memoized_add({"key": "value"})
        elif input_type == tuple:
            memoized_add((1, 2))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_utils_memoize_1_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_utils_memoize_1_test_invalid_input.py:4:0: E0401: Unable to import 'pymonent.utils' (import-error)


"""