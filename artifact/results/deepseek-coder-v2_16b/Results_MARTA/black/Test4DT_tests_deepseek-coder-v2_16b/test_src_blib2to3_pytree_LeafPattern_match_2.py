
import pytest
from blib2to3.pytree import LeafPattern

def test_valid_type():
    leaf_pattern = LeafPattern(type=123)
    assert leaf_pattern.type == 123

def test_invalid_type():
    with pytest.raises(AssertionError):
        LeafPattern(type=256)

def test_valid_content():
    leaf_pattern = LeafPattern(content="print('Hello, World!')", type=5)
    assert leaf_pattern.content == "print('Hello, World!')"

def test_invalid_content_type():
    with pytest.raises(AssertionError):
        LeafPattern(content=256, type=5)

def test_valid_name():
    leaf_pattern = LeafPattern(type=123, name="identifier")
    assert leaf_pattern.name == "identifier"
