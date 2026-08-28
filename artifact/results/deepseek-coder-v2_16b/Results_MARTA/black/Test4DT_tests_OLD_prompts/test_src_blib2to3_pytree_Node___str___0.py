
import pytest
from blib2to3.pytree import Node


def test_invalid_type():
    with pytest.raises(AssertionError):
        Node(type=255, children=[], context='invalid_context')


