
import pytest
from pymonet.either import Left, Right

def test_invalid_input():
    # Arrange
    invalid_input = 'invalid'
    
    # Act
    left_instance = Left(invalid_input)
    
    # Assert
    assert left_instance.is_left() is True
