
import pytest
import collections
from pytutils.trees import tree

def test_valid_input():
    my_tree = tree()
    assert isinstance(my_tree, collections.defaultdict)
    assert isinstance(my_tree['root'], collections.defaultdict)
