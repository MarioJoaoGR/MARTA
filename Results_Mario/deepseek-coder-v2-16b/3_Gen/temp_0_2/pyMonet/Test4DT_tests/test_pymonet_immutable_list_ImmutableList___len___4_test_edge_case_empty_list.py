
import pytest
from pymonet.immutable_list import ImmutableList

def test_edge_case_empty_list():
    # Arrange
    empty_list = ImmutableList()
    
    # Act & Assert
    assert len(empty_list) == 0, "The length of an empty list should be 0"
