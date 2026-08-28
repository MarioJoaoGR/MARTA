
# Module: blib2to3.pytree
# test_blib2to3.py
from blib2to3.pytree import Node
import pytest

@pytest.fixture
def valid_node():
    return Node(258, [Node(256, []), Node(257, [])])

@pytest.fixture
def node_with_fixers():
    fixers_applied_list = [1, 2, 3]
    return Node(261, [Node(260, [])], fixers_applied=fixers_applied_list)

@pytest.fixture
def node_with_context():
    context_info = {"key": "value"}
    return Node(264, [Node(263, [])], context=context_info)

@pytest.fixture
def node_with_prefix():
    return Node(266, [Node(265, [])], prefix="example_prefix")

def test_node_creation_valid(valid_node):
    assert valid_node.type == 258
    assert len(valid_node.children) == 2
    for child in valid_node.children:
        assert child.parent is valid_node

def test_node_creation_with_fixers(node_with_fixers):
    assert node_with_fixers.type == 261
    assert len(node_with_fixers.children) == 1
    for child in node_with_fixers.children:
        assert child.parent is node_with_fixers