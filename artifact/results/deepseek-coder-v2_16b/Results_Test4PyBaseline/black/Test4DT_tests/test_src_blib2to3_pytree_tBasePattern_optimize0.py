
import pytest
from blib2to3.pytree import BasePattern, LeafPattern, NodePattern, WildcardPattern

# Test creating instances of BasePattern subclasses
def test_create_leaf_pattern():
    leaf_pattern = LeafPattern(type=1, content="example_content")
    assert isinstance(leaf_pattern, LeafPattern)
    assert leaf_pattern.type == 1