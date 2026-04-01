
import pytest
from pymonet.monad_try import Try  # Assuming this is the correct module path

def test_valid_case():
    success_try = Try('success', True)
    
    def binder(val):
        return Try(val + " bound", True)
    
    # Test successful bind
    result = success_try.bind(binder)
    assert result.value == 'success bound'
    
    # Create a failed Try instance
    failure_try = Try(None, False)
    
    # Test bind on a failed Try instance
    result = failure_try.bind(binder)
    assert result.value is None
