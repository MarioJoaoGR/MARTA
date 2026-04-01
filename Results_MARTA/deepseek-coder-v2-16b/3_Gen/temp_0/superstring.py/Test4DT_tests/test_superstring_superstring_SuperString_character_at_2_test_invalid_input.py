
import pytest
from superstring.superstring import SuperString

def test_invalid_input():
    superstring = SuperString('Hello, World!')
    
    # Test when start_index is out of bounds
    with pytest.raises(IndexError):
        superstring.character_at(len(superstring._content))  # len(superstring._content) is the length of the string
