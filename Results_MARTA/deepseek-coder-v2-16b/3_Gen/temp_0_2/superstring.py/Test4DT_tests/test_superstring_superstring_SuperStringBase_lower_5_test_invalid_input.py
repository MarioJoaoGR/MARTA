
import pytest
from superstring.superstring import SuperStringBase, SUPERSTRING_MINIMAL_LENGTH

def test_invalid_input():
    with pytest.raises(TypeError):
        s = SuperStringBase('This is a longer string with more than 20 characters')
