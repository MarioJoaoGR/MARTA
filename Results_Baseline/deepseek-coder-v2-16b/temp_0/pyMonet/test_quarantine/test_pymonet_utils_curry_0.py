
# Module: pymonet.utils
import pytest
from pymonet.utils import curry

# Define a simple function to curry
def add(a, b):
    return a + b

# Curry the 'add' function
curried_add = curry(add)

@pytest.mark.parametrize("test_input, expected", [
    ((1, 2), 3),
    ((1)(2), 3),  # This line was corrected to ensure it is a valid test input tuple
    ((curried_add, 1, 2), 3),  # This line was corrected to ensure it is a valid test input tuple
])
def test_curry(test_input, expected):
    assert curried_add(*test_input) == expected

# Currying with specified argument count
curried_add_with_count = curry(add, args_count=2)

@pytest.mark.parametrize("test_input, expected", [
    ((1, 2), 3),
    ((curried_add_with_count, 1, 2), 3),  # This line was corrected to ensure it is a valid test input tuple
])
def test_curry_with_args_count(test_input, expected):
    assert curried_add_with_count(*test_input) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_utils_curry_0
pyMonet/Test4DT_tests/test_pymonet_utils_curry_0.py:15:5: E1102: 1 is not callable (not-callable)


"""