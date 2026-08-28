
import pytest
from typing import Callable, List, Tuple

# Assuming the cond function is defined in a module named pymonet.utils
# from pymonet.utils import cond

def cond(condition_list: List[Tuple[Callable[[T], bool], Callable]]):
    def result(*args):
        for (condition_function, execute_function) in condition_list:
            if condition_function(*args):
                return execute_function(*args)
    return result

# Test scenarios
def test_condition_true():
    def is_even(n):
        return n % 2 == 0
    
    def double(n):
        return n * 2
    
    cond_func = cond([
        (is_even, double),
        (lambda n: n > 5, lambda n: n * 3)
    ])
    
    assert cond_func(4) == 8
    assert cond_func(7) == 21

def test_condition_false():
    def is_even(n):
        return n % 2 == 0
    
    def double(n):
        return n * 2
    
    cond_func = cond([
        (is_even, double),
        (lambda n: n > 5, lambda n: n * 3)
    ])
    
    assert cond_func(3) == 9
    assert cond_func(6) == 12

def test_multiple_conditions():
    def is_positive(n):
        return n > 0
    
    def square(n):
        return n * n
    
    cond_func = cond([
        (is_even, lambda n: n * 2),
        (is_positive, square),
        (lambda n: n < -10, lambda n: -n)
    ])
    
    assert cond_func(4) == 8
    assert cond_func(7) == 49
    assert cond_func(-12) == 12

def test_no_condition_met():
    def always_false(n):
        return False
    
    cond_func = cond([
        (always_false, lambda n: n * 2)
    ])
    
    with pytest.raises(TypeError):
        cond_func(5)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
________________ ERROR collecting test_pymonet_utils_cond_0.py _________________
/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_cond_0.py:8: in <module>
    def cond(condition_list: List[Tuple[Callable[[T], bool], Callable]]):
E   NameError: name 'T' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_cond_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""