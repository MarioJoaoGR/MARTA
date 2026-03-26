
import pytest
from pymonet.lazy import Lazy

def test_valid_input():
    lazy = Lazy(lambda x: x * x)
    assert lazy.to_either(10).value == 100
