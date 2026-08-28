
import pytest
from pymonet.maybe import Maybe

def test_get_or_else_with_empty_value():
    maybe_empty = Maybe(value=None, is_nothing=True)
    assert maybe_empty.get_or_else("default") == "default"
