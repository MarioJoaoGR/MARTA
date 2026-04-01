
import pytest
from flutes.iterator import chunk

def test_edge_case():
    with pytest.raises(ValueError):
        list(chunk(-1, range(5)))
