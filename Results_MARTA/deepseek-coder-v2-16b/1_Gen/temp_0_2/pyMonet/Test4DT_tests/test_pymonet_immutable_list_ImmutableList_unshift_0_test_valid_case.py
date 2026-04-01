
from pymonet.immutable_list import ImmutableList  # Assuming the module path is correct

def test_valid_case():
    empty_list = ImmutableList.empty()
    assert empty_list.is_empty == True
    
    new_list = empty_list.unshift(1)
    assert new_list.head == 1
    assert new_list.tail.is_empty == True
