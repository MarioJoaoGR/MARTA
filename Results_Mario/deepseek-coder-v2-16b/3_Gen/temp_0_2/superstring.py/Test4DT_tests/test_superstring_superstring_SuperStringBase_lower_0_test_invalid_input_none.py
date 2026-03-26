
import pytest
from superstring.superstring import SuperStringBase, SuperString, SuperStringLower

# Assuming SUPERSTRING_MINIMAL_LENGTH is defined somewhere in the module 'superstring.superstring'
SUPERSTRING_MINIMAL_LENGTH = 10  # Placeholder for where it might be defined

def test_invalid_input_none():
    with pytest.raises(TypeError):
        s = SuperStringBase(None)
        s.lower()
