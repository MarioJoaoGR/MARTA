
import pytest
from blib2to3.pytree import Node


def test_post_order():
    root = Node(type=256, children=[], context='root')
    child1 = Node(type=257, children=[], context='child1')
    child2 = Node(type=258, children=[], context='child2')
    root.children = [child1, child2]

    post_order_nodes = list(root.post_order())
    assert len(post_order_nodes) == 3
    assert post_order_nodes[0] is child1
    assert post_order_nodes[1] is child2
    assert post_order_nodes[2] is root