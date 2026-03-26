
import pytest
from pymonet.lazy import Lazy

def test_ap():
    # Create a Lazy instance with a function that doubles its input
    lazy_double = Lazy(lambda x: x * 2)
    
    # Create another Lazy instance with a function that adds 1 to its input
    lazy_add_one = Lazy(lambda x: x + 1)
    
    # Apply the double function to the add one function using ap method
    result = lazy_double.ap(lazy_add_one)
    
    # Check if the result is a new Lazy instance with the composed function
    assert isinstance(result, Lazy)
    
    # Fold the result to get the final value and check it
    folded_value = result.fold(1)
    assert folded_value == 4  # Since (1 + 1) * 2 = 4

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy_ap_0_test_valid_inputs
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_ap_0_test_valid_inputs.py:19:19: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""