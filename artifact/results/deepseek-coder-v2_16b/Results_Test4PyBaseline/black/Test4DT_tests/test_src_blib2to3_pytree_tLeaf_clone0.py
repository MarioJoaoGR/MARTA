
import pytest
from blib2to3.pytree import Leaf

# Test initialization with basic parameters
def test_leaf_initialization_basic():
    leaf = Leaf(type=1, value='example_value')
    assert leaf.type == 1
    assert leaf.value == 'example_value'
    assert leaf._prefix == ''
    assert leaf.lineno == 0
    assert leaf.column == 0
    assert leaf.fixers_applied == []