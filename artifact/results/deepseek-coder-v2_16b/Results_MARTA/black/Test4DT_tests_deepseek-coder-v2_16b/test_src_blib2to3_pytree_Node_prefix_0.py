
import pytest
from blib2to3.pytree import Node


def test_invalid_input_type():
    with pytest.raises(AssertionError):
        Node(type=255, children=[], context='example_context', prefix='example_prefix', fixers_applied=['fixer1', 'fixer2'])