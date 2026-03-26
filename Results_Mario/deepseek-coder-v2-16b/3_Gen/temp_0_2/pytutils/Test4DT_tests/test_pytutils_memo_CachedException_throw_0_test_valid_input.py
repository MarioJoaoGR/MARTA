
import pytest
from pytutils.memo import CachedException  # Assuming this is the correct module path

def test_valid_input():
    ex = ValueError("This is a test error")
    cached_exception = CachedException(ex)
    
    with pytest.raises(ValueError) as exc_info:
        cached_exception.throw()
        
    assert str(exc_info.value) == "This is a test error"
