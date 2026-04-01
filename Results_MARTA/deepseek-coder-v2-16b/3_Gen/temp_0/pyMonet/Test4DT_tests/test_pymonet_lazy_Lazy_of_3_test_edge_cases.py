
from pymonet.lazy import Lazy
import pytest

def test_edge_cases():
    none_input = Lazy(None)
    assert none_input.constructor_fn is None
