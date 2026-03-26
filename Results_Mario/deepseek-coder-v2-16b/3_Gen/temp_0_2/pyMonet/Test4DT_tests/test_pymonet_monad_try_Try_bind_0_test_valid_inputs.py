
import pytest
from pymonet.monad_try import Try

def test_valid_inputs():
    success = Try(10, True)
    
    def double(x):
        return Try(x * 2, True)
    
    result = success.bind(double)
    assert result.value == 20
