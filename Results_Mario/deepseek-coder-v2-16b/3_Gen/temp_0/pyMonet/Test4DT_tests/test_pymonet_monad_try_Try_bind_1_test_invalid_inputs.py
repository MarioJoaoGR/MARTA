
import pytest
from pymonet.monad_try import Try

def test_invalid_inputs():
    with pytest.raises(TypeError):
        success_try = Try("success", True)
        invalid_bind = success_try.bind(123)  # Passing an integer instead of a function
