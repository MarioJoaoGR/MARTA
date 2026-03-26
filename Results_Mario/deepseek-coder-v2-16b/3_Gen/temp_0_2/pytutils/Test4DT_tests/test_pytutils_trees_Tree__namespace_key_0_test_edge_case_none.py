
import pytest
from pytutils.trees import Tree

def test_edge_case_none():
    tree = Tree(None, 'namespace')
    
    # Check that the tree is initialized correctly without any data
    assert not hasattr(tree, 'data')
    assert tree.namespace == 'namespace'
