
import pytest
from superstring import SuperString

def test_edge_case():
    # Test with an empty string
    s = SuperString('')
    with pytest.raises(IndexError):
        s.character_at(0)  # Should raise IndexError for out of bounds access on an empty string
    
    # Test with a non-empty string but invalid index
    s = SuperString("Hello, World!")
    with pytest.raises(IndexError):
        s.character_at(13)  # Should raise IndexError as the index is out of bounds
