
import pytest
from pytutils.trees import get_tree_node, set_tree_node



def test_invalid_key():
    mapping = {}
    with pytest.raises(ValueError):
        set_tree_node(mapping, 'b', 1)