
import pytest
from pymonet.utils import increase

def test_invalid_input():
    with pytest.raises(TypeError):
        increase("string")
