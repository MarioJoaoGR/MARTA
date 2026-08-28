
import pytest
from blib2to3.pytree import LeafPattern

def test_valid_init_with_type():
    pattern = LeafPattern(type=123)
    assert pattern.type == 123


def test_valid_init_with_content():
    pattern = LeafPattern(content="print('Hello, World!')", type=5)
    assert pattern.content == "print('Hello, World!')"
    assert pattern.type == 5

def test_invalid_init_with_non_string_content():
    with pytest.raises(AssertionError):
        LeafPattern(content=12345, type=5)

def test_valid_init_with_name():
    pattern = LeafPattern(type=123, name="identifier")
    assert pattern.name == "identifier"