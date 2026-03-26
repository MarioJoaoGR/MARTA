
import pytest
from pymonet.utils import curried_map

def test_invalid_input_none():
    with pytest.raises(TypeError):
        curried_map(lambda x: x * 2, None)
