
import pytest
from blib2to3.pytree import Node

@pytest.fixture
def child1():
    return Node(type=257, children=[], context='left_child', prefix='example_prefix', fixers_applied=['fixer1', 'fixer2'])

@pytest.fixture
def child2():
    return Node(type=258, children=[], context='right_child', prefix='example_prefix', fixers_applied=['fixer3', 'fixer4'])

@pytest.fixture
def parent_node(child1, child2):
    return Node(type=256, children=[child1, child2])

@pytest.fixture
def new_child():
    return Node(type=259, children=[], context='new_child', prefix='example_prefix', fixers_applied=['fixer5'])

def test_valid_insertion(parent_node, new_child):
    parent_node.insert_child(1, new_child)
    assert len(parent_node.children) == 3
    assert parent_node.children[1] is new_child
    assert new_child.parent is parent_node

def test_edge_case_empty_list():
    empty_parent = Node(type=256, children=[])
    new_child = Node(type=259, children=[], context='new_child', prefix='example_prefix', fixers_applied=['fixer5'])
    empty_parent.insert_child(0, new_child)
    assert len(empty_parent.children) == 1
    assert empty_parent.children[0] is new_child
    assert new_child.parent is empty_parent

def test_invalid_input():
    parent_node = Node(type=256, children=[])
    with pytest.raises(AssertionError):
        new_child = Node(type=255, children=[], context='invalid_child', prefix='example_prefix', fixers_applied=['fixer5'])
        parent_node.insert_child(0, new_child)
