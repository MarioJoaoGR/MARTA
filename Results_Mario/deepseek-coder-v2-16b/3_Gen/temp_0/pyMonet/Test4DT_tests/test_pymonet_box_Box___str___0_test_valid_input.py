
from pymonet.box import Box

def test_valid_input():
    # Arrange
    value = 123
    box = Box(value)
    
    # Act & Assert
    assert str(box) == 'Box[value={}]'.format(value)
