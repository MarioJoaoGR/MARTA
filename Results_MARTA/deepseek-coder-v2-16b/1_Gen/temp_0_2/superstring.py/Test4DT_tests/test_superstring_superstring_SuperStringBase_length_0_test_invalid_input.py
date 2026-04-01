
import pytest
from superstring.superstring import SuperStringBase

def test_invalid_input():
    with pytest.raises(TypeError):
        super_string = SuperStringBase(None)
