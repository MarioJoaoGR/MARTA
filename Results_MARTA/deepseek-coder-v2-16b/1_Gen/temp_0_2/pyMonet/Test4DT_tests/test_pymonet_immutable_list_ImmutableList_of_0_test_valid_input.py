
from pymonet.immutable_list import ImmutableList

def test_valid_input():
    # Creating an immutable list with elements 1, 2, 3
    my_list = ImmutableList.of(1, 2, 3)
    
    assert my_list.head == 1
    assert my_list.tail.head == 2
    assert my_list.tail.tail.head == 3
    assert not my_list.is_empty
