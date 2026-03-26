
import pytest
from pymonet.monad_try import Try

def test_invalid_input():
    with pytest.raises(TypeError):
        success_try = Try("success", True)
        invalid_bind = success_try.bind(None)  # Passing a non-callable object to simulate an invalid input
