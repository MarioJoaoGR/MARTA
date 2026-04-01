
import pytest
from pymonet.monad_try import Try  # Assuming this is a hypothetical module

def test_valid_input():
    try_instance = Try(10, True)
    
    def success_callback(value):
        assert value == 10
    
    result = try_instance.on_success(success_callback)
    assert result is try_instance
