
import pytest
from pymonet.monad_try import Try  # Assuming this is a hypothetical module, adjust accordingly

def test_valid_inputs():
    success = Try(10, True)
    failure = Try('Error', False)
    
    assert str(success) == 'Try[value=10, is_success=True]'
    assert str(failure) == 'Try[value=Error, is_success=False]'
