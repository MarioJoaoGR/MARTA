
import pytest
from pymonet.immutable_list import ImmutableList

def test_empty_creation():
    empty_list = ImmutableList.empty()
    assert empty_list.is_empty is True
    assert empty_list.head is None
    assert empty_list.tail is None
