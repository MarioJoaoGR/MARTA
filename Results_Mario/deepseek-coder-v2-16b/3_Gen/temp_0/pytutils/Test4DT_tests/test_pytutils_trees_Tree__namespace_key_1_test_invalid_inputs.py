
import pytest
from pytutils.trees import Tree

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Passing an invalid argument (a list instead of a dictionary) should raise TypeError
        Tree([1, 2, 3])
