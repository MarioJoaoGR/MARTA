
import pytest
from pymonet.either import Left, Right

def test_invalid_input():
    with pytest.raises(TypeError):
        Left().map(lambda x: x)
