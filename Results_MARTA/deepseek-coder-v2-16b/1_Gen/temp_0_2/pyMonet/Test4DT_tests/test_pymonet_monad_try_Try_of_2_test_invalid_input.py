
import pytest
from pymonet.monad_try import Try  # Assuming this is the correct module for Try monad

def test_invalid_input():
    def invalid_function():
        return None
    
    with pytest.raises(Exception):
        result = Try.of(invalid_function)
        assert not result.is_success
        assert isinstance(result.value, Exception)
