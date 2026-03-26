
from pymonet.either import Either, Left, Right
from pymonet.lazy import Lazy
import pytest

def test_edge_case():
    # Create an instance of Either with a value
    either = Either(Right("success"))
    
    # Call the to_lazy method and check if it returns a Lazy monad
    lazy_either = either.to_lazy()
    
    # Check that the Lazy monad encapsulates a function returning the original value
    assert lazy_either.f() == "success"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Either_to_lazy_0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_either_Either_to_lazy_0_test_edge_case.py:14:11: E1101: Instance of 'Lazy' has no 'f' member; maybe 'of'? (no-member)


"""