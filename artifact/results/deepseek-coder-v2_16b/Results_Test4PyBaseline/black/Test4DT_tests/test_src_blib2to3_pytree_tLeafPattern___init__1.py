# Module: blib2to3.pytree
import pytest
from blib2to3.pytree import LeafPattern

# Test case 1: Creating a pattern that matches any leaf node with type 123
def test_leafpattern_type():
    pattern = LeafPattern(type=123)
    assert pattern.type == 123

# Test case 2: Creating a pattern that matches any leaf node containing the string "example"
def test_leafpattern_content():
    pattern = LeafPattern(content="example")
    assert pattern.content == "example"

# Test case 3: Creating a pattern that matches any leaf node and stores it under the name "print_statement" in results
def test_leafpattern_name():
    pattern = LeafPattern(name="print_statement")
    assert pattern.name == "print_statement"

# Test case 4: Ensuring an error is raised when type is not within the valid range (0 <= type < 256)
def test_leafpattern_invalid_type():
    with pytest.raises(AssertionError):
        LeafPattern(type=256)

# Test case 5: Ensuring an error is raised when content is not a string
def test_leafpattern_invalid_content():
    with pytest.raises(AssertionError):
        LeafPattern(content=123)

