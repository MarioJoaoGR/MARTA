
import pytest
import collections
from pytutils.trees import tree

def test_tree_creation():
    my_tree = tree()
    assert isinstance(my_tree, collections.defaultdict)
    assert isinstance(my_tree['new_key'], collections.defaultdict)

def test_nested_structure():
    my_tree = tree()
    my_tree['parent']['child'] = 'value'
    assert my_tree == {'parent': {'child': 'value'}}
