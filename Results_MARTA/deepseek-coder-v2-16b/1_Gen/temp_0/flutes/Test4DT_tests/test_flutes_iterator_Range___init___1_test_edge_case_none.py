
import pytest
from flutes.iterator import Range

def test_edge_case_none():
    with pytest.raises(ValueError):
        r = Range()
