
# Module: pytutils.trees
# test_trees.py
from pytutils.trees import Tree
import pytest

@pytest.fixture
def empty_tree():
    return Tree()

@pytest.fixture
def populated_tree():
    return Tree({'a': 1, 'b': {'c': 2}})

@pytest.fixture
def ref_tree():
    return Tree(initial={'a': 1, 'b': {'c': 2}}, initial_is_ref=True)

def test_init_without_parameters(empty_tree):
    assert isinstance(empty_tree, Tree)