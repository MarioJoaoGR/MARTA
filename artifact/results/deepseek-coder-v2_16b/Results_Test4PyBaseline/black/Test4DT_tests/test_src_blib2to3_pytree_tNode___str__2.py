
# Module: blib2to3.pytree
import pytest
from blib2to3.pytree import Node

# Test creating a root node with two children
def test_create_root_node_with_two_children():
    child1 = Node(type=256, children=[], context="example_context")  # Create a child node with type 256
    child2 = Node(type=257, children=[], context="example_context")  # Create another child node with type 257
    root = Node(type=258, children=[child1, child2])  # Create the root node with children
    
    assert root.type == 258
    assert len(root.children) == 2
    assert root.children[0] is child1
    assert root.children[1] is child2
    assert child1.parent is root
    assert child2.parent is root

# Test creating a root node without specifying fixers_applied
def test_create_root_node_without_fixers_applied():
    child1 = Node(type=256, children=[], context="example_context")  # Create a child node with type 256
    child2 = Node(type=257, children=[], context="example_context")  # Create another child node with type 257
    root = Node(type=258, children=[child1, child2])  # Create the root node with children
    
    assert root.fixers_applied is None

# Test creating a root node with specified fixers_applied
def test_create_root_node_with_specified_fixers_applied():
    fixers_list = [1, 2, 3]  # Example list of applied fixers
    child1 = Node(type=256, children=[], context="example_context")  # Create a child node with type 256
    child2 = Node(type=257, children=[], context="example_context")  # Create another child node with type 257
    root = Node(type=258, children=[child1, child2], fixers_applied=fixers_list)  # Create the root node with children and specified fixers
    