
import pytest
from blib2to3.pytree import Leaf

# Test cases for initializing a Leaf object

def test_basic_initialization():
    leaf = Leaf(type=1, value='example_value')
    assert leaf.type == 1
    assert leaf.value == 'example_value'
    assert leaf._prefix == ''
    assert leaf.lineno == 0
    assert leaf.column == 0
    assert leaf.fixers_applied == []
    assert leaf.children == []

def test_initialization_with_context():
    with pytest.raises(TypeError):
        Leaf(type=1, value='example_value', context=(10, 30))

def test_initialization_with_prefix():
    leaf = Leaf(type=1, value='example_value', prefix='prefix_')
    assert leaf.type == 1
    assert leaf.value == 'example_value'
    assert leaf._prefix == 'prefix_'
    assert leaf.lineno == 0
    assert leaf.column == 0
    assert leaf.fixers_applied == []
    assert leaf.children == []

def test_initialization_with_fixers_applied():
    leaf = Leaf(type=1, value='example_value', fixers_applied=[{'fixer': 'fix_example'}])
    assert leaf.type == 1
    assert leaf.value == 'example_value'
    assert leaf._prefix == ''
    assert leaf.lineno == 0
    assert leaf.column == 0
    assert leaf.fixers_applied == [{'fixer': 'fix_example'}]