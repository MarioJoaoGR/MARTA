
import pytest
from pymonet.lazy import Lazy

def test_ap():
    # Create a Lazy instance with a function that doubles its input
    lazy_double = Lazy(lambda x: 2 * x)
    
    # Create another Lazy instance with a function that triples its input
    lazy_triple = Lazy(lambda x: 3 * x)
    
    # Apply the double function to the triple function using ap method
    result = lazy_double.ap(lazy_triple)
    
    # Check if the result is a new Lazy instance with the composed function
    assert isinstance(result, Lazy)
    
    # Fold the result to get the final value
    folded_value = result.fold(10)
    
    # Check if the folded value is correct after applying both functions
    assert folded_value == 2 * (3 * 10)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy_ap_0_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_ap_0_test_edge_cases.py:19:19: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""