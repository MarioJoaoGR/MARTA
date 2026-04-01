
import pytest
from pymonet.immutable_list import ImmutableList

def test_none_input():
    lst = ImmutableList()
    result = lst.find(lambda x: x is None)
    assert result is None, "Expected None for an empty list"
