
import pytest
from superstring.superstring import SuperStringBase

def test_invalid_strip():
    with pytest.raises(TypeError):
        s = SuperStringBase("  Hello, World!  ")
        s.strip()
