
import pytest
from pymonet.utils import curry

def add(a, b):
    return a + b

@pytest.mark.parametrize("args_count", [2])
@pytest.mark.parametrize("x", [add])
def test_valid_inputs(args_count, x):
    curried_add = curry(x, args_count=args_count)
    if args_count == 2:
        assert curried_add(1)(2) == add(1, 2)
    elif args_count == 3:
        curried_add_three = curry(x, args_count=3)
        assert curried_add_three(1)(2)(3) == add(1, 2, 3)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_utils_fn_0_test_valid_inputs
pyMonet/Test4DT_tests/test_pymonet_utils_fn_0_test_valid_inputs.py:16:45: E1121: Too many positional arguments for function call (too-many-function-args)


"""