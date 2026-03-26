
import pytest
from pytutils.memo import CachedException  # Assuming this is the correct module path

def test_edge_case():
    class CustomError(Exception):
        pass
    
    ex = CustomError("An error occurred")
    cached_exception = CachedException(ex)
    
    with pytest.raises(CustomError) as exc_info:
        cached_exception.throw()
        
    assert isinstance(exc_info.value, CustomError)
    assert str(exc_info.value) == "An error occurred"
