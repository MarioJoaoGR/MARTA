
# Module: blib2to3.pytree
import pytest
from blib2to3.pytree import Node

# Test creating a Node without Children
def test_create_node_without_children():
    root = Node(type=258, children=[], prefix="root_prefix", fixers_applied=["fixer1"])
    assert root.type == 258
    assert root.children == []