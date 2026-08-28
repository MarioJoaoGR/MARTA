
# test_src_blib2to3_pytree_Node___repr___.py
from blib2to3.pytree import Node
import pytest


def test_invalid_type():
    with pytest.raises(AssertionError):
        Node(type=255, children=[], context='example_context', prefix='example_prefix', fixers_applied=['fixer1', 'fixer2'])

def test_no_fixers_applied():
    child1 = Node(type=257, children=[], context='example_context', prefix='example_prefix')
    assert child1.fixers_applied is None