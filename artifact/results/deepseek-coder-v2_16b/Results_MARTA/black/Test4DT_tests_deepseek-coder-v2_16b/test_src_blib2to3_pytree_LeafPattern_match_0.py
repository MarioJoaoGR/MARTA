
import pytest
from blib2to3.pytree import LeafPattern

# Test valid inputs
def test_valid_inputs():
    leaf_pattern = LeafPattern(type=123, content='example_content', name='example_name')
    assert leaf_pattern.type == 123
    assert leaf_pattern.content == 'example_content'
    assert leaf_pattern.name == 'example_name'

# Test edge cases
def test_edge_cases():
    leaf_pattern = LeafPattern()
    assert leaf_pattern.type is None
    assert leaf_pattern.content is None
    assert leaf_pattern.name is None

# Test invalid inputs
def test_invalid_inputs():
    with pytest.raises(AssertionError):
        leaf_pattern = LeafPattern(type=256, content='example_content')
    
    with pytest.raises(AssertionError):
        leaf_pattern = LeafPattern(type=123, content=123)
