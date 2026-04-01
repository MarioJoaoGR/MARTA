
import pytest
from pytutils.trees import set_tree_node

def test_invalid_input():
    mapping = {'a': {'b': {}}}
    
    # Test setting a value with an invalid key (e.g., no colon present)
    with pytest.raises(ValueError):
        set_tree_node(mapping, 'ab', 1)
