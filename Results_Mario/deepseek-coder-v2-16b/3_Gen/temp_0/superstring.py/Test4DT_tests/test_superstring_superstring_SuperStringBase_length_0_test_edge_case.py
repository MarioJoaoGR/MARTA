
import pytest
from superstring import SuperString

def test_edge_case():
    # Test with None input to check error handling
    with pytest.raises(TypeError):
        s = SuperString(None)
        assert s.length() == 0
