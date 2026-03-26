
import pytest
from flutes.iterator import scanl, scanr

def test_edge_case_empty_list():
    # Test when the iterable is an empty list
    with pytest.raises(RuntimeError):
        result = scanr(lambda x, y: x + y, [])
