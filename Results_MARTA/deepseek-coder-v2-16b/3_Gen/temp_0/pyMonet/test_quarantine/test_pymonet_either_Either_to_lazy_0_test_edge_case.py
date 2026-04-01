
import pytest
from pymonet.either import Either
from pymonet.lazy import Lazy

def test_edge_case():
    either = Either(5)  # Creates a Right with value 5
    lazy_either = either.to_lazy()  # Converts the Either to a Lazy monad
    
    assert isinstance(lazy_either, Lazy)
    assert lazy_either.fold() == 5

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Either_to_lazy_0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_either_Either_to_lazy_0_test_edge_case.py:11:11: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""