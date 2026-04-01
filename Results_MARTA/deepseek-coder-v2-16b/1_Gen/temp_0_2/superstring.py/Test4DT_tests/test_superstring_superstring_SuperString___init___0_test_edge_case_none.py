
import pytest
from superstring.superstring import SuperString

def test_edge_case_none():
    # Setup
    superstring_instance = SuperString(None)
    
    # Test that split method raises a TypeError when content is None
    with pytest.raises(TypeError):
        superstring_instance.split()
