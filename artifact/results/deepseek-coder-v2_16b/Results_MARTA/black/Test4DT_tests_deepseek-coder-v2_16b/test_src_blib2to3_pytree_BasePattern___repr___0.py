
import pytest
from blib2to3.pytree import BasePattern, LeafPattern, NodePattern, WildcardPattern

def test_leafpattern_can_be_instantiated():
    leaf_pattern = LeafPattern(type=123, content="example_content", name="identifier")
    assert isinstance(leaf_pattern, LeafPattern)


def test_wildcardpattern_can_be_instantiated():
    wildcard_pattern = WildcardPattern(content="example_content")
    assert isinstance(wildcard_pattern, WildcardPattern)