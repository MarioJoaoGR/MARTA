
import pytest
from pymonet.monad_try import Try

def test_valid_inputs():
    # Test successful Try object
    success_try = Try('success', True)
    def binder(val):
        return Try(val + " bound", True)
    
    assert success_try.bind(binder).value == 'success bound'
    
    # Test failed Try object
    failure_try = Try(None, False)
    assert failure_try.bind(binder).value is None
