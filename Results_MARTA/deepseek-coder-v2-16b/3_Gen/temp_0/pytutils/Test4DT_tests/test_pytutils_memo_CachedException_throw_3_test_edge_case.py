
import pytest
from pytutils.memo import CachedException

def test_edge_case():
    class CustomError(Exception):
        pass
    
    ex = CustomError("An error occurred")
    cached_exception = CachedException(ex)
    
    with pytest.raises(CustomError) as excinfo:
        cached_exception()  # Call the instance to trigger the throw method
    
    assert str(excinfo.value) == "An error occurred"
