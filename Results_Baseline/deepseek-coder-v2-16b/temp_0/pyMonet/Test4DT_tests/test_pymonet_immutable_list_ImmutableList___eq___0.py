
# Module: pymonet.immutable_list
# Import the function from its module
from pymonet.immutable_list import ImmutableList

def test_init_default():
    # Test initialization with default values
    empty_list = ImmutableList()
    assert empty_list.head is None
    assert empty_list.tail is None