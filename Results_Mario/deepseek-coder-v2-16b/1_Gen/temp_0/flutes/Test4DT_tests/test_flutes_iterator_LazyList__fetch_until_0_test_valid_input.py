
import pytest
from flutes.iterator import LazyList  # Assuming this is the correct import path

def test_valid_input():
    # Arrange
    data = [1, 2, 3, 4, 5]
    lazy_list = LazyList(data)
    
    # Act & Assert
    for i in range(len(data)):
        assert next(lazy_list.iter) == data[i]
