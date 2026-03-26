
import pytest
from pytutils.trees import set_tree_node, get_tree_node

def test_invalid_input():
    tree = {'a': {'b': {}}}
    
    # Test with an empty string as the key
    with pytest.raises(ValueError):
        set_tree_node(tree, '', 'value')
