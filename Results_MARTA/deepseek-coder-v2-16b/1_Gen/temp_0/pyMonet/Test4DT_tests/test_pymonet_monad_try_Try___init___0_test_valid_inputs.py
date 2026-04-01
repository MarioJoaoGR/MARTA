
import pytest
from pymonet.monad_try import Try

def test_valid_inputs():
    # Test initialization with valid inputs
    successful_try = Try(42, is_success=True)
    failed_try = Try("Operation failed", is_success=False)
    
    assert successful_try.is_success == True
    assert successful_try.value == 42
    
    assert failed_try.is_success == False
    assert failed_try.value == "Operation failed"
