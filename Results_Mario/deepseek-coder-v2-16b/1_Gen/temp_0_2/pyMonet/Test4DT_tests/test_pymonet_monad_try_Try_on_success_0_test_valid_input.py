
import pytest
from pymonet.monad_try import Try

def test_valid_input():
    try_instance = Try(value='Success', is_success=True)
    
    def success_callback(val):
        assert val == 'Success'
    
    result = try_instance.on_success(success_callback)
    assert result.value == 'Success'
    assert result.is_success == True
