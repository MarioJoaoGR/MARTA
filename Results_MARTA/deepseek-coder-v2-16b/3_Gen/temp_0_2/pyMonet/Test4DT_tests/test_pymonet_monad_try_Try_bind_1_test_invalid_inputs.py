
import pytest
from pymonet.monad_try import Try

def test_invalid_inputs():
    with pytest.raises(TypeError):
        success_try = Try("success", True)
        result = success_try.bind(None)  # Passing a non-function should raise TypeError
