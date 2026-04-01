
from pymonet.immutable_list import ImmutableList

def test_none_input():
    empty_list = ImmutableList.empty()
    assert empty_list.is_empty is True
    assert empty_list.head is None
    assert empty_list.tail is None
