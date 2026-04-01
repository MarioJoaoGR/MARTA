
import pytest
from pymonet.lazy import Lazy

def test_none_input():
    lazy = Lazy(lambda x: x if x is not None else 0)
    assert lazy.constructor_fn(None) == 0
