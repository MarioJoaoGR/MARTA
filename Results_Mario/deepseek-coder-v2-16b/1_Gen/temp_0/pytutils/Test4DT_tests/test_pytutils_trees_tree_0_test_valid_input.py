
import pytest
import collections
from pytutils.trees import tree

@pytest.fixture(scope="module")
def nested_tree():
    return tree()

def test_valid_input(nested_tree):
    assert isinstance(nested_tree, collections.defaultdict)
    assert isinstance(nested_tree['key'], collections.defaultdict)
    assert len(nested_tree) == 1
