
import pytest
from pymonet.lazy import Lazy

def test_edge_case():
    lazy = Lazy(lambda x: x * x)
    with pytest.raises(TypeError):  # Since the function expects arguments but None is passed, it should raise a TypeError
        assert lazy.to_either(None).is_left()
