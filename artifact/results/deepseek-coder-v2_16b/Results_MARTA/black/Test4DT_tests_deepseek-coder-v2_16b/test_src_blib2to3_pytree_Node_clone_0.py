
import pytest
from blib2to3.pytree import Node

def test_valid_init():
    child1 = Node(type=257, children=[], context='left_child', prefix='example_prefix', fixers_applied=['fixer1'])
    assert child1.type >= 256, "Type must be greater than or equal to 256"
    for ch in child1.children:
        assert ch.parent is None, repr(ch)
        ch.parent = child1
    child1.invalidate_sibling_maps()

def test_edge_init():
    with pytest.raises(TypeError):
        parent_node = Node(type=None, children=[])
