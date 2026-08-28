
import pytest
from blib2to3.pytree import LeafPattern  # Corrected import statement

# Test case for creating a LeafPattern with type 123
def test_leaf_pattern_with_type():
    pattern = LeafPattern(type=123)
    assert isinstance(pattern, LeafPattern), "The object should be an instance of LeafPattern"
    assert pattern.type == 123, "The type attribute should be set to 123"

# Test case for creating a LeafPattern with content "example"
def test_leaf_pattern_with_content():
    pattern = LeafPattern(content="example")
    assert isinstance(pattern, LeafPattern), "The object should be an instance of LeafPattern"
    assert pattern.content == "example", "The content attribute should be set to 'example'"

# Test case for creating a LeafPattern with name "print_statement"
def test_leaf_pattern_with_name():
    pattern = LeafPattern(name="print_statement")
    assert isinstance(pattern, LeafPattern), "The object should be an instance of LeafPattern"