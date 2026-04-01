
import pytest
from superstring.superstring import SuperStringBase

def test_edge_cases():
    # Test with None
    with pytest.raises(TypeError):
        base_string_none = SuperStringBase(None)
