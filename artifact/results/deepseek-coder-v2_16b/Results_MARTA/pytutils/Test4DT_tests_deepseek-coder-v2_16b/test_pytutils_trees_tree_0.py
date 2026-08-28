
import pytest
import collections
from pytutils.trees import tree

def test_valid_input():
    my_tree = tree()
    assert isinstance(my_tree, collections.defaultdict)
    assert isinstance(my_tree['parent'], collections.defaultdict)

def test_edge_case_none():
    with pytest.raises(TypeError):
        tree(None)

def test_error_handling():
    my_tree = tree()
    assert isinstance(my_tree, collections.defaultdict)
