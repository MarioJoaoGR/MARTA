
import pytest
from blib2to3.pytree import LeafPattern

# Test valid input with type and content
def test_valid_input_with_type_and_content():
    leaf_pattern = LeafPattern(type=123, content='print("Hello, World!")', name='identifier')
    assert leaf_pattern.type == 123
    assert leaf_pattern.content == 'print("Hello, World!")'
    assert leaf_pattern.name == 'identifier'

# Test valid input without specifying content but with type
def test_valid_input_without_content():
    leaf_pattern = LeafPattern(type=123)
    assert leaf_pattern.type == 123
    assert leaf_pattern.content is None
    assert leaf_pattern.name is None

# Test invalid input with incorrect type
def test_invalid_input_with_incorrect_type():
    with pytest.raises(AssertionError):
        leaf_pattern = LeafPattern(type=256, content='print("Hello, World!")', name='identifier')
