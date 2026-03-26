
import pytest
from superstring.superstring import SuperStringBase, SUPERSTRING_MINIMAL_LENGTH

def test_invalid_input():
    with pytest.raises(TypeError):
        super_string = SuperStringBase(None)
