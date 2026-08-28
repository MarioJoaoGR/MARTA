
import pytest
from pymonet.utils import pipe

def test_invalid_inputs():
    with pytest.raises(TypeError):
        pipe("string", lambda x: x + 1)
