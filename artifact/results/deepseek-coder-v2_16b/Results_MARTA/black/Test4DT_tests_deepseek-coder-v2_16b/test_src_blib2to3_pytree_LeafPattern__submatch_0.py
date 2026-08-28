
import pytest
from blib2to3.pytree import LeafPattern

def test_valid_leafpattern_with_type():
    leaf_pattern = LeafPattern(type=123)
    assert leaf_pattern.type == 123
    assert leaf_pattern.content is None
    assert leaf_pattern.name is None

def test_valid_leafpattern_with_type_and_name():
    leaf_pattern = LeafPattern(type=123, name="identifier")
    assert leaf_pattern.type == 123
    assert leaf_pattern.content is None
    assert leaf_pattern.name == "identifier"

def test_valid_leafpattern_with_content():
    leaf_pattern = LeafPattern(content="print('Hello, World!')", type=5)
    assert leaf_pattern.type == 5
    assert leaf_pattern.content == "print('Hello, World!')"
    assert leaf_pattern.name is None

def test_invalid_input_type_out_of_range():
    with pytest.raises(AssertionError):
        LeafPattern(type=256)

def test_invalid_input_content_not_string():
    with pytest.raises(AssertionError):
        LeafPattern(content=[1, 2, 3])
