
from pymonet.lazy import Lazy

def test_standard_input():
    lazy = Lazy.of(5)
    assert isinstance(lazy, Lazy)
