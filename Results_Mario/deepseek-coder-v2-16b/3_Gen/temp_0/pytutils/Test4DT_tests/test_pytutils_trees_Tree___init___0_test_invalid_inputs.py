
import pytest
from pytutils.trees import Tree

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test initializing the Tree class with invalid input type for initial
        Tree(initial=123, namespace='test', initial_is_ref=False)
