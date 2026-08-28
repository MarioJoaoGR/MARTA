
import pytest
import collections
from pytutils.trees import tree

# Test the creation of a nested dictionary structure using `collections.defaultdict`
def test_tree_creation():
    my_tree = tree()
    assert isinstance(my_tree, collections.defaultdict)
    assert isinstance(my_tree['root'], collections.defaultdict)
    assert isinstance(my_tree['root']['subroot'], collections.defaultdict)

# Test accessing elements in the nested dictionary structure
def test_nested_access():
    my_tree = tree()
    my_tree['root']['subroot'] = 'value'
    assert my_tree['root']['subroot'] == 'value'

# Test that calling `tree()` multiple times returns new instances of defaultdict
def test_multiple_instances():
    instance1 = tree()
    instance2 = tree()
    assert isinstance(instance1, collections.defaultdict)
    assert isinstance(instance2, collections.defaultdict)
    assert id(instance1) != id(instance2)  # Ensure different instances

# Test the base case where calling `tree()` directly returns a defaultdict with type 'function'
def test_base_case():
    my_tree = tree()
    assert isinstance(my_tree, collections.defaultdict)