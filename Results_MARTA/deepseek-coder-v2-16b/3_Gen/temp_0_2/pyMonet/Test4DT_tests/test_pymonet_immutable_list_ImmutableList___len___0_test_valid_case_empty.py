
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_case_empty():
    empty_list = ImmutableList()
    assert len(empty_list) == 0, "Expected length of an empty list to be 0"
