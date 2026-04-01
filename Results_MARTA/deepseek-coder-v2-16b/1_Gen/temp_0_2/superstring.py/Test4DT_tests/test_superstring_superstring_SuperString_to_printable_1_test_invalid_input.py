
import pytest
from superstring.superstring import SuperString

def test_invalid_input():
    # Test with None as content
    with pytest.raises(TypeError):
        SuperString(None).to_printable()
    
    # Test with a non-string type (e.g., int)
    with pytest.raises(TypeError):
        SuperString(12345).to_printable()
