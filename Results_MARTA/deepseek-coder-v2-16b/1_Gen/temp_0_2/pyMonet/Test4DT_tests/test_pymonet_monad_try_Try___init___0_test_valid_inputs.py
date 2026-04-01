
import pytest
from pymonet.monad_try import Try

def test_valid_inputs():
    success = Try("Success", True)
    failure = Try(None, False)
    
    assert success.value == "Success"
    assert success.is_success is True
    assert failure.value is None
    assert failure.is_success is False
