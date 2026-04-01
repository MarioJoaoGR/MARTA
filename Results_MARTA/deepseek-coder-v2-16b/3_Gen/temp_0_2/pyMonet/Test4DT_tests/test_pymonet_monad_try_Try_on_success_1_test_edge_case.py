
import pytest
from pymonet.monad_try import Try

def test_on_success():
    success = Try(10, True)
    
    def print_value(val):
        assert val == 10
    
    result = success.on_success(print_value)
    assert result.is_success is True
    assert result.value == 10

def test_on_failure():
    failure = Try(None, False)
    
    def print_value(val):
        pytest.fail("This should not be called because the operation failed.")
    
    result = failure.on_success(print_value)
    assert result.is_success is False
    assert result.value is None
