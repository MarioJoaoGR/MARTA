
import pytest
from typing import Text, List, Optional, Set, Any

# Assuming the module name is 'blib2to3.pytree' and the class is defined within it
from blib2to3.pytree import Leaf

def test_leaf_basic():
    leaf = Leaf(type=1, value='example_value')
    assert leaf.type == 1
    assert leaf.value == 'example_value'
    assert leaf.lineno == 0
    assert leaf.column == 0
    assert leaf.fixers_applied == []