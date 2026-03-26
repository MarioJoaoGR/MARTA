
import pytest
from pymonet.utils import curried_map

def test_edge_case_empty_list():
    # Arrange
    mapper = lambda x: x * 2
    collection = []
    
    # Act
    result = curried_map(mapper, collection)
    
    # Assert
    assert result == [], "Expected an empty list when the input collection is empty"
