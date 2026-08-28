
import pytest
from pytutils.trees import Tree

# Test initialization with no initial data and default parameters
def test_tree_initialization_no_data():
    tree = Tree()
    assert isinstance(tree, Tree)
    assert not hasattr(tree, 'data')  # Since it's initialized without data, `data` should not be present
    assert tree.namespace == ''

# Test initialization with a nested dictionary
def test_tree_initialization_with_nested_dict():
    initial = {'a': 1, 'b': {'c': 2}}
    tree = Tree(initial)
    assert isinstance(tree, Tree)