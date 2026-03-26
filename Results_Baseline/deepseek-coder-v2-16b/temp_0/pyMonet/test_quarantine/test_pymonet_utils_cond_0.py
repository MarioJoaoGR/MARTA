
# Module: pymonet.utils
import pytest
from typing import Callable, List, Tuple

# Import the function from its module
from pymonet.utils import cond

def test_cond_basic():
    def is_even(n):
        return n % 2 == 0
    
    def double(n):
        return n * 2
    
    cond_func = cond([
        (is_even, double),
        (lambda n: n > 5, lambda n: n * 3)
    ])
    
    assert cond_func(4) == 8  # Output: 8 (double since 4 is even)
    assert cond_func(7) == 21 # Output: 21 (triple since 7 is greater than 5)

def test_cond_different_conditions():
    def is_positive(n):
        return n > 0
    
    def square(n):
        return n * n
    
    cond_func = cond([
        (is_even, double),
        (is_positive, square),
        (lambda n: n < -10, lambda n: n + 10)
    ])
    
    assert cond_func(4) == 8   # Output: 8 (double since 4 is even)
    assert cond_func(7) == 49  # Output: 49 (square since 7 is positive)
    assert cond_func(-12) == 2 # Output: 2 (add 10 since -12 is less than -10)

def test_cond_multiple_conditions():
    def is_multiple_of_three(n):
        return n % 3 == 0
    
    def triple(n):
        return n * 3
    
    cond_func = cond([
        (is_even, double),
        (is_multiple_of_three, triple),
        (lambda n: n < 0, lambda n: -n)
    ])
    
    assert cond_func(6) == 12   # Output: 12 (double since 6 is even)
    assert cond_func(9) == 27   # Output: 27 (triple since 9 is a multiple of three)
    assert cond_func(-15) == -15# Output: -15 (negate since -15 is negative)

def test_cond_no_condition_met():
    def always_false(n):
        return False
    
    def do_nothing(*args):
        return None
    
    cond_func = cond([
        (always_false, do_nothing),
        (lambda n: n > 10, lambda n: n * 2)
    ])
    
    assert cond_func(5) is None # Output: None since no condition is met

def test_cond_raise_error():
    def always_true(n):
        return True
    
    with pytest.raises(TypeError):
        cond([
            (always_true, lambda n: n + 1)
        ])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_utils_cond_0
pyMonet/Test4DT_tests/test_pymonet_utils_cond_0.py:32:9: E0602: Undefined variable 'is_even' (undefined-variable)
pyMonet/Test4DT_tests/test_pymonet_utils_cond_0.py:32:18: E0602: Undefined variable 'double' (undefined-variable)
pyMonet/Test4DT_tests/test_pymonet_utils_cond_0.py:49:9: E0602: Undefined variable 'is_even' (undefined-variable)
pyMonet/Test4DT_tests/test_pymonet_utils_cond_0.py:49:18: E0602: Undefined variable 'double' (undefined-variable)


"""