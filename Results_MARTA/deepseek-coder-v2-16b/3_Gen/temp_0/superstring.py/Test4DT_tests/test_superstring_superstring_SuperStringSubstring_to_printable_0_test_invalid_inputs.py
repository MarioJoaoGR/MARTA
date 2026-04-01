
import pytest
from superstring.superstring import SuperStringSubstring

def test_invalid_inputs():
    with pytest.raises(TypeError):
        ss = SuperStringSubstring("Hello, World!", "invalid", 12)
        ss.to_printable()
