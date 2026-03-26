
import pytest
from superstring.superstring import SuperStringBase, SUPERSTRING_MINIMAL_LENGTH

class TestSuperStringBase:
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            super_string = SuperStringBase("Hello, World!")
            substring = super_string.substring(-1, 5)  # Invalid start index
