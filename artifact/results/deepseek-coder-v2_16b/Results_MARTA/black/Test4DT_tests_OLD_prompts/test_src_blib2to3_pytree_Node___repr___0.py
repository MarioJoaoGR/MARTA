
import pytest
from blib2to3.pytree import Node



def test_invalid_input():
    with pytest.raises(AssertionError):
        Node(type=256 - 1, children=[], context='example_context', prefix='example_prefix', fixers_applied=['fixer1', 'fixer2'])