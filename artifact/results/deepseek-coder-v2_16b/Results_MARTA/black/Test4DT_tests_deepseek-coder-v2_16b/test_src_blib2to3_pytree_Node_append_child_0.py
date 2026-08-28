
import pytest
from blib2to3.pytree import Node

def test_valid_input():
    child1 = Node(type=257, children=[], context='left_child')
    parent_node = Node(type=256, children=[child1])
    assert parent_node.type == 256
    assert len(parent_node.children) == 1
    assert parent_node.children[0] is child1
    assert child1.parent is parent_node

def test_edge_case():
    with pytest.raises(TypeError):
        Node(type=None, children=[])
