
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_input():
    empty_list = ImmutableList()
    new_list = empty_list.unshift(1)
    assert not empty_list.is_empty, "The original list should be non-empty after unshifting a value."
    assert new_list.head == 1, "The head of the new list should be the inserted value."
    assert isinstance(new_list.tail, ImmutableList), "The tail of the new list should be an instance of ImmutableList."
