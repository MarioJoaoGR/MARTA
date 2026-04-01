
import pytest
from superstring.superstring import SuperStringBase

def test_invalid_strip():
    # Arrange
    non_string_input = None
    with pytest.raises(TypeError):
        super_string = SuperStringBase(non_string_input)
