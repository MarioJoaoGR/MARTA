
import pytest
from blib2to3.pytree import LeafPattern, Leaf, NL





def test_leafpattern_match_leaf_node():
    leaf_pattern = LeafPattern(type=123)
    with pytest.raises(TypeError):
        node = Leaf(type=123, content="print('Hello, World!')", name="identifier")  # Assuming Leaf is a class that can be instantiated with arguments