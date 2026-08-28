
import pytest
from blib2to3.pytree import Node


def test_clone():
    original_node = Node(type=256, children=[Node(type=257, children=[])])
    cloned_node = original_node.clone()
    
    assert isinstance(cloned_node, Node)
    assert cloned_node.type == 256
    assert len(cloned_node.children) == 1
    assert cloned_node.children[0].type == 257
    assert cloned_node.fixers_applied is None