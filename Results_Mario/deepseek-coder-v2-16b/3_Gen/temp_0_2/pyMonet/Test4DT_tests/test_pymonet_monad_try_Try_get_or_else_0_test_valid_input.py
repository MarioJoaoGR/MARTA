
import pytest
from pymonet.monad_try import Try

def test_valid_input():
    success_try = Try(10, True)
    assert success_try.get_or_else(0) == 10
    
    failure_try = Try(None, False)
    assert failure_try.get_or_else("default") == "default"
