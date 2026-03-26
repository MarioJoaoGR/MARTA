
import collections
import pytest
from pytutils.trees import tree

def test_tree_returns_defaultdict():
    """Test that the tree function returns an instance of defaultdict."""
    result = tree()
    assert isinstance(result, collections.defaultdict)
