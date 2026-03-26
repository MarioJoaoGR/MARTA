
import pytest
from pymonet.either import Either, Left, Right
from pymonet.lazy import Lazy

def test_valid_input():
    # Create an Either instance with a valid value
    either = Either(5)
    
    # Convert the Either to a Lazy monad
    lazy_either = either.to_lazy()
    
    # Check if the conversion was successful by evaluating the stored function and checking the result
    assert lazy_either.fold() == 5

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Either_to_lazy_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_either_Either_to_lazy_0_test_valid_input.py:14:11: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""