
import pytest
from blib2to3.pytree import LeafPattern

# Test initialization with only type specified
def test_valid_input_with_type_only():
    leaf_pattern = LeafPattern(type=123)
    assert leaf_pattern.type == 123
    assert leaf_pattern.content is None
    assert leaf_pattern.name is None

# Test initialization with both type and name specified
def test_valid_input_with_type_and_name():
    leaf_pattern = LeafPattern(type=123, name='identifier')
    assert leaf_pattern.type == 123
    assert leaf_pattern.content is None
    assert leaf_pattern.name == 'identifier'

# Test initialization with content specified
def test_valid_input_with_content():
    leaf_pattern = LeafPattern(content='print("Hello, World!")', type=5)
    assert leaf_pattern.type == 5
    assert leaf_pattern.content == 'print("Hello, World!")'
    assert leaf_pattern.name is None
