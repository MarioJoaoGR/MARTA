
import pytest
from pymonet.semigroups import First

def test_valid_case_1():
    # Arrange
    f1 = First(1)
    f2 = First(2)
    
    # Act
    combined = f1.concat(f2)
    
    # Assert
    assert combined.value == 1
