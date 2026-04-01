
import pytest
from superstring.superstring import SuperStringBase, SUPERSTRING_MINIMAL_LENGTH

def test_invalid_input_none():
    base_string = SuperStringBase()
    base_string._value = None
    
    with pytest.raises(TypeError):
        base_string.upper()
