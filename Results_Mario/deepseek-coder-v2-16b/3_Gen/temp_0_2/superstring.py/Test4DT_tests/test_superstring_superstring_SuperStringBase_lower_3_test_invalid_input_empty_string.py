
import pytest
from superstring.superstring import SuperStringBase, SuperString, SuperStringLower

def test_invalid_input_empty_string():
    with pytest.raises(TypeError):
        s = SuperStringBase('')
