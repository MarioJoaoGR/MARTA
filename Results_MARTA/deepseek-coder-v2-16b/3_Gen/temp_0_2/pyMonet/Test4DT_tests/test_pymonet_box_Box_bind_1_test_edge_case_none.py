
import pytest
from pymonet.box import Box

def test_edge_case_none():
    # Arrange
    box = Box(None)
    
    # Act & Assert
    with pytest.raises(TypeError):
        # Attempt to bind a function to None, which should raise a TypeError
        result = box.bind(lambda x: x * 2)
