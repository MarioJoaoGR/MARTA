
import pytest
from superstring.superstring import SuperString

def test_invalid_input():
    superstring = SuperString('Hello, World!')
    with pytest.raises(IndexError):
        superstring.character_at(100)  # This index is out of the valid range for the given string
