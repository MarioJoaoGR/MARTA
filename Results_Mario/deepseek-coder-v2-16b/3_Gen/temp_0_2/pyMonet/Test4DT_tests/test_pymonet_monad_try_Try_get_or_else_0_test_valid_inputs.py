
import pytest
from pymonet.monad_try import Try

def test_valid_inputs():
    # Test a successful Try object
    success = Try(10, True)
    assert success.get_or_else(0) == 10
    
    # Test a failed Try object
    failure = Try("error", False)
    assert failure.get_or_else("default") == "default"
