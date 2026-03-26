
import pytest
from sty import RgbFg

def test_valid_input():
    # Arrange
    r, g, b = 0, 255, 0
    
    # Act
    color = RgbFg(r, g, b)
    
    # Assert
    assert color.args == [r, g, b]
