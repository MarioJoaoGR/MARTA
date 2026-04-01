
import pytest
from pymonet.monad_try import Try  # Assuming this module exists and contains the Try class

def test_invalid_input():
    try_instance = Try(10, True)
    
    with pytest.raises(TypeError):
        try_instance.on_success("not a function")
