
import pytest
from pymonet.lazy import Lazy

def test_edge_case():
    lazy = Lazy(None)
    with pytest.raises(TypeError):
        lazy.get()
