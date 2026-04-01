
import pytest
import collections
from pytutils.trees import tree

def test_edge_case():
    my_tree = tree()
    assert isinstance(my_tree, collections.defaultdict)
    assert isinstance(my_tree['key'], collections.defaultdict)
