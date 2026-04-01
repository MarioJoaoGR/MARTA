
import pytest
from pytutils.trees import set_tree_node, get_tree_node

def test_missing_key():
    mapping = {}
    with pytest.raises(ValueError):
        set_tree_node(mapping, 'a:b:c', 1)
