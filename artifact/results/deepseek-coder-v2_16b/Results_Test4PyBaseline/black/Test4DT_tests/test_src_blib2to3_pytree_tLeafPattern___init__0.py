# Module: blib2to3.pytree
import pytest
from blib2to3.pytree import LeafPattern

# Test case 1: Creating a pattern that matches any leaf node with type 123
def test_leafpattern_type():
    pattern = LeafPattern(type=123)
    assert pattern.type == 123, f"Expected type to be 123 but got {pattern.type}"

# Test case 2: Creating a pattern that matches any leaf node containing the string "example"
def test_leafpattern_content():
    pattern = LeafPattern(content="example")
    assert pattern.content == "example", f"Expected content to be 'example' but got {pattern.content}"

# Test case 3: Creating a pattern that matches any leaf node and stores it under the name "print_statement" in results
def test_leafpattern_name():
    pattern = LeafPattern(name="print_statement")
    assert pattern.name == "print_statement", f"Expected name to be 'print_statement' but got {pattern.name}"

# Test case 4: Creating a pattern with an invalid type (should raise an assertion error)
def test_leafpattern_invalid_type():
    with pytest.raises(AssertionError):
        LeafPattern(type=-1)

# Test case 5: Creating a pattern with an invalid content (should raise an assertion error)
def test_leafpattern_invalid_content():
    with pytest.raises(AssertionError):
        LeafPattern(content=123)

# Test case 6: Creating a pattern without any parameters and checking default values
def test_leafpattern_default():
    pattern = LeafPattern()
    assert pattern.type is None, f"Expected type to be None but got {pattern.type}"
    assert pattern.content is None, f"Expected content to be None but got {pattern.content}"
    assert pattern.name is None, f"Expected name to be None but got {pattern.name}"
