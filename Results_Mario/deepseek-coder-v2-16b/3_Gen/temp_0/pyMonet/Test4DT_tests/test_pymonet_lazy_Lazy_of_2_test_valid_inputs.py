
import pytest
from pymonet.lazy import Lazy

def test_standard_input():
    square = lambda x: x * x
    lazy = Lazy(square)
    assert lazy.constructor_fn(5) == 25
