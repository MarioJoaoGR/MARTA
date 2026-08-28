
import pytest
from typing import List, Optional, Text, Any

# Assuming the module name is 'blib2to3.pytree' and the Node class is imported correctly from it
from blib2to3.pytree import Node

def test_node_creation():
    child1 = Node(256, [])  # Create a child node with type 256
    child2 = Node(257, [])  # Create another child node with type 257
    root = Node(258, [child1, child2])  # Create the root node with children
    
    assert root.type == 258
    assert len(root.children) == 2
    assert root.children[0].type == 256
    assert root.children[1].type == 257
    assert root.children[0].parent is root
    assert root.children[1].parent is root

def test_node_creation_with_prefix():
    child1 = Node(256, [])  # Create a child node with type 256
    child2 = Node(257, [])  # Create another child node with type 257
    root = Node(258, [child1, child2], prefix='public')  # Create the root node with children and a prefix
    
    assert root.type == 258
    assert len(root.children) == 2
    assert root.children[0].type == 256
    assert root.children[1].type == 257