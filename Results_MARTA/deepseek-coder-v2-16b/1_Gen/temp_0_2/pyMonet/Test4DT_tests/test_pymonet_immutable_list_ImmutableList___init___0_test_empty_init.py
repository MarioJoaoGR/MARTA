
from pymonet.immutable_list import ImmutableList  # Importing correctly from the module 'pymonet.immutable_list'
import pytest

def test_empty_init():
    empty_list = ImmutableList.empty()
    assert empty_list.is_empty is True
    assert empty_list.head is None
    assert empty_list.tail is None
