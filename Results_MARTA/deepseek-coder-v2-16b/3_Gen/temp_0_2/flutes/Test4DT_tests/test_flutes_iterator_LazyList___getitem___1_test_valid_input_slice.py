
import pytest
from flutes.iterator import LazyList

def test_valid_input_slice():
    # Arrange
    lazy_list = LazyList([1, 2, 3, 4, 5])
    
    # Act & Assert
    assert lazy_list[0] == 1
    assert lazy_list[1] == 2
    assert lazy_list[2] == 3
    assert lazy_list[3] == 4
    assert lazy_list[4] == 5
    
    # Slice test
    assert lazy_list[:] == [1, 2, 3, 4, 5]
    assert lazy_list[1:3] == [2, 3]
    assert lazy_list[::2] == [1, 3, 5]
