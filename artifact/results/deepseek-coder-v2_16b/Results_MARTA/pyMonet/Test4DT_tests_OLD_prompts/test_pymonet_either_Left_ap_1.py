
import pytest
from pymonet.either import Left, Right

def test_invalid_inputs():
    with pytest.raises(TypeError):
        Left().ap(None)
