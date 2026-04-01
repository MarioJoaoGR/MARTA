
import pytest
from pymonet.utils import increase

def test_edge_case_none():
    # Test when value is None (should raise a TypeError)
    with pytest.raises(TypeError):
        assert increase(None) == 1
