
import pytest
from pytutils.memo import CachedException

def test_edge_case():
    class CustomError(Exception):
        pass
    
    ex = CustomError("An error occurred")
    cached_exception = CachedException(ex)
    
    with pytest.raises(CustomError) as exc_info:
        cached_exception.throw()
        
    assert str(exc_info.value) == "An error occurred"
