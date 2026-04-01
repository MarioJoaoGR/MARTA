
from superstring.superstring import SuperStringBase, SuperStringUpper
import pytest

def test_invalid_input():
    # Setup
    with pytest.raises(TypeError):
        super_string = SuperStringUpper(SuperStringBase('Hello, World!'))
