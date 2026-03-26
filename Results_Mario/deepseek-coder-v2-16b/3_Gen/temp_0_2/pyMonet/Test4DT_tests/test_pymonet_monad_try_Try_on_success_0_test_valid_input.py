
import pytest
from pymonet.monad_try import Try

def test_valid_input():
    success = Try(10, True)
    
    def print_value(val):
        assert val == 10
    
    result = success.on_success(print_value)
    assert result.is_success is True
