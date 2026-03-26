
import pytest
from pymonet.maybe import Maybe

def test_valid_input():
    maybe = Maybe(value=42, is_nothing=False)
    assert maybe.get_or_else(default_value=0) == 42
