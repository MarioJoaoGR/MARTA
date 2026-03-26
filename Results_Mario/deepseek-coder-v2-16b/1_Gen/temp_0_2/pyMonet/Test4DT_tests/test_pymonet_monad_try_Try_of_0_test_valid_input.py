
import pytest
from pymonet.monad_try import Try

def test_valid_input():
    def safe_function(x):
        return x + 1
    
    result = Try.of(safe_function, 5)
    assert result.value == 6
    assert result.is_success is True
