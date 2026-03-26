
import pytest
from flutes.iterator import Range

def test_edge_case_none():
    r = Range(10)
    with pytest.raises(TypeError):
        assert r[None] == 9  # Assuming the last element should be accessed when index is None
