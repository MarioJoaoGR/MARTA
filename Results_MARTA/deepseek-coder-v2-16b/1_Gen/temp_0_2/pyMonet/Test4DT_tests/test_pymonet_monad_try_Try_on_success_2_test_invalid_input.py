
import pytest
from pymonet.monad_try import Try

def test_invalid_input():
    try_instance = Try(value='Invalid', is_success=True)
    
    # Providing a non-function to on_success should raise an error
    with pytest.raises(TypeError):
        try_instance.on_success('not_a_function')
