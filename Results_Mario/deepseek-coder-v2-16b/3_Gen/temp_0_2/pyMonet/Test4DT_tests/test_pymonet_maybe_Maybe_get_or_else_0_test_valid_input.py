
import pytest
from pymonet.maybe import Maybe

def test_valid_input():
    maybe = Maybe(10, False)
    assert maybe.get_or_else(0) == 10
