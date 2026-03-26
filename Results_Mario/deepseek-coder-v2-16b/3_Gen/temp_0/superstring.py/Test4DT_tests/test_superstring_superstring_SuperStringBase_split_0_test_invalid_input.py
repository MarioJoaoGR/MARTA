
import pytest
from superstring.superstring import SuperStringBase

def test_invalid_input():
    with pytest.raises(TypeError):
        invalid_string = SuperStringBase('InvalidInput')
        invalid_string.split()  # This should raise a TypeError because the method expects an argument for separator
