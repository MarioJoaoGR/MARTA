
import pytest
from pymonet import utils  # Assuming the module is named pymonet and contains a utils module

# Define a mock function for testing
def add(a, b):
    return a + b

@pytest.fixture
def curried_add():
    return utils.fn(add)

def test_curried_add_partially_applied(curried_add):
    assert curried_add(1)(2) == 3

def test_curried_add_fully_applied(curried_add):
    assert curried_add(1, 2) == 3

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_utils_fn_0_test_valid_case_two_arguments
pyMonet/Test4DT_tests/test_pymonet_utils_fn_0_test_valid_case_two_arguments.py:11:11: E1101: Module 'pymonet.utils' has no 'fn' member (no-member)


"""