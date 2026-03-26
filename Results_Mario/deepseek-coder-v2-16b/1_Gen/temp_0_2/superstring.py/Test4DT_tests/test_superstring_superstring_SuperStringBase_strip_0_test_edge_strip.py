
import pytest
from superstring.superstring import SuperStringBase

def test_edge_strip():
    # Test case 1: Empty string
    with pytest.raises(TypeError):
        super_string = SuperStringBase('')
