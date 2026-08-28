
import pytest
from typing import Text, List, Optional, Set, Any

# Assuming the module name is 'blib2to3' for the purpose of this test case
from blib2to3.pytree import Leaf

def test_leaf_initialization():
    leaf = Leaf(type=123, value='example_value')
    assert leaf.type == 123
    assert leaf.value == 'example_value'
    assert leaf._prefix == ''
    assert leaf.fixers_applied == []