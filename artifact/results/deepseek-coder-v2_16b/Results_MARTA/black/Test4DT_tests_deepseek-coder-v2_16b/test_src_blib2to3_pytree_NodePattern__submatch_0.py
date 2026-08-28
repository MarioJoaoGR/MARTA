
import pytest
from blib2to3.pytree import NodePattern, BasePattern, WildcardPattern, Node

def test_init_with_invalid_content():
    with pytest.raises(AssertionError):
        NodePattern(type=257, content="not a list")
