
import pytest
from blib2to3.pytree import Node

# Test creating a root node with children
def test_create_root_node_with_children():
    child1 = Node(type=256, children=[], context="left_child")
    child2 = Node(type=257, children=[], context="right_child")
    root = Node(type=258, children=[child1, child2])
    
    assert root.type == 258
    assert len(root.children) == 2
    assert root.children[0] is child1
    assert root.children[1] is child2
    assert root.children[0].parent is root
    assert root.children[1].parent is root

# Test creating a root node with children and specific prefix
def test_create_root_node_with_prefix():
    child1 = Node(type=256, children=[], context="left_child", prefix="L")
    child2 = Node(type=257, children=[], context="right_child", prefix="R")
    root = Node(type=258, children=[child1, child2], prefix="root_prefix")
    
    assert root.type == 258
    assert len(root.children) == 2
    assert root.children[0] is child1
    assert root.children[1] is child2
    assert root.children[0].parent is root
    assert root.children[1].parent is root