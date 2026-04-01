
import pytest
from pymonet.lazy import Lazy

def test_edge_case_none():
    lazy = Lazy(lambda x: x)  # Dummy function to avoid TypeError during initialization
    with pytest.raises(TypeError):
        lazy.to_box()
