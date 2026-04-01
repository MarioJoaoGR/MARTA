
from pymonet.lazy import Lazy

def test_edge_cases():
    none_input = Lazy(None)
    assert none_input.constructor_fn is None
