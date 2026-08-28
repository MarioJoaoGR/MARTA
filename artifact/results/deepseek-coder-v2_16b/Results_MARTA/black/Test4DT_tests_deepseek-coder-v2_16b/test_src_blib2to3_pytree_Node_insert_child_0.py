
import pytest
from blib2to3.pytree import Node


def test_insert_child():
    child = Node(type=257, children=[], context="left_child", prefix="example_prefix", fixers_applied=["fixer1", "fixer2"])
    parent_node = Node(type=256, children=[child])
    
    new_child = Node(type=259, children=[], context="new_child", prefix="example_prefix", fixers_applied=["fixer5"])
    parent_node.insert_child(1, new_child)
    
    assert len(parent_node.children) == 2
    assert parent_node.children[1] == new_child
    assert new_child.parent == parent_node

def test_invalid_type():
    with pytest.raises(AssertionError):
        Node(type=255, children=[], context='valid_context', prefix='example_prefix', fixers_applied=['fixer1'])