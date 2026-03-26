
import pytest
from superstring.superstring import SuperStringBase

def test_invalid_input():
    with pytest.raises(TypeError) as excinfo:
        superstring_instance = SuperStringBase(None)
    assert str(excinfo.value) == "SuperStringBase() takes no arguments"
