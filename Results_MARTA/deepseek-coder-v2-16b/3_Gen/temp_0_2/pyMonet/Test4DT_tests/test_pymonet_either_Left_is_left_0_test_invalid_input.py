
import pytest
from pymonet.either import Left, Right

def test_invalid_input():
    # Arrange
    non_left_instance = None
    
    # Act and Assert
    with pytest.raises(TypeError):
        if not isinstance(non_left_instance, Left):
            raise TypeError("Expected an instance of Left")
