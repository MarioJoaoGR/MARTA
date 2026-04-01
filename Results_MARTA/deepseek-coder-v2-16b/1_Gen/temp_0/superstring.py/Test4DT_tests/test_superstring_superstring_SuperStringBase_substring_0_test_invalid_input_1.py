
import pytest
from superstring.superstring import SuperStringBase, SuperString, SuperStringSubstring

def test_invalid_input_1():
    with pytest.raises(TypeError):
        s = SuperStringBase('Hello, World!')
