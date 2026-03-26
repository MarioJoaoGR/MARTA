
import pytest
from superstring.superstring import SuperString, SuperStringLower

# Test initialization with default content
def test_initialization_with_default_content():
    base_content = SuperString("Hello, World!")
    obj = SuperStringLower(base_content)
    assert str(obj) == "hello, world!"

# Test initialization with specific content
def test_initialization_with_specific_content():
    base_content = SuperString("This is a Test String.")
    obj = SuperStringLower(base_content)
    assert str(obj) == "this is a test string."

# Test to_printable with no parameters (entire string in lowercase)
def test_to_printable_no_parameters():
    base_content = SuperString("Hello, World!")
    obj = SuperStringLower(base_content)
    assert obj.to_printable() == "hello, world!"

# Test to_printable with specified indices
def test_to_printable_with_indices():
    base_content = SuperString("Hello, World!")
    obj = SuperStringLower(base_content)