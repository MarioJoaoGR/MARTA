
import pytest
from pytutils.trees import Tree, set_tree_node

def test_valid_input():
    tree = Tree()
    with pytest.raises(ValueError):
        tree['a'] = 'b'
