
import pytest
from blib2to3.pytree import Leaf
from typing import Text, List, Optional, Set, Any


def test_invalid_type():
    with pytest.raises(AssertionError):
        Leaf(type=256, value='example', context=(1, 2), prefix='prefix', fixers_applied=['fixer1'])


def test_with_prefix():
    leaf = Leaf(type=1, value='example', prefix='custom_prefix')
    assert leaf.prefix == 'custom_prefix'
