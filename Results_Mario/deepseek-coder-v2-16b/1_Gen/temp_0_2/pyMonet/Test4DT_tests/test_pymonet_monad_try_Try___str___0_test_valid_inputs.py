
import pytest
from pymonet.monad_try import Try  # Assuming this is the correct module for Try

def test_valid_inputs():
    success = Try('Success', True)
    failure = Try(None, False)
    
    assert str(success) == 'Try[value=Success, is_success=True]'
    assert str(failure) == 'Try[value=None, is_success=False]'
