
import pytest
from blib2to3.pytree import LeafPattern

# Test valid input with type and content
def test_valid_input_with_type_and_content():
    leaf_pattern = LeafPattern(type=123, content='print("Hello, World!")', name='identifier')
    assert leaf_pattern.type == 123
    assert leaf_pattern.content == 'print("Hello, World!")'
    assert leaf_pattern.name == 'identifier'

# Test valid input with only type specified
def test_valid_input_with_only_type():
    leaf_pattern = LeafPattern(type=123)
    assert leaf_pattern.type == 123
    assert leaf_pattern.content is None
    assert leaf_pattern.name is None

# Test invalid input when content is not a string
def test_invalid_input_content_not_string():
    with pytest.raises(AssertionError):
        LeafPattern(type=123, content=123)
