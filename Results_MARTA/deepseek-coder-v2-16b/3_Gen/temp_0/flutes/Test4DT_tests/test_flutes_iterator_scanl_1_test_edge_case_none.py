
import pytest
from flutes.iterator import scanl

def test_edge_case_none():
    # Arrange
    func = lambda acc, x: acc + x if x is not None else acc
    initial = 0
    
    # Act and Assert
    with pytest.raises(TypeError):
        list(scanl(func, None, initial))
