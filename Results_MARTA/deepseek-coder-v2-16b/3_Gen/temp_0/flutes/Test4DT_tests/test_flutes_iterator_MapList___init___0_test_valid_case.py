
import pytest
from flutes.iterator import MapList

def test_valid_case():
    # Arrange
    a = [1, 2, 3, 4, 5]
    func = lambda x: x * x
    maplist = MapList(func, a)
    
    # Act & Assert
    assert maplist[0] == 1
    assert maplist[1] == 4
    assert maplist[2] == 9
    assert maplist[3] == 16
    assert maplist[4] == 25
