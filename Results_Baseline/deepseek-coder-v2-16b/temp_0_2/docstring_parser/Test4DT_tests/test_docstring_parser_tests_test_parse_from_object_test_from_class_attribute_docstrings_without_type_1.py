
import pytest
from docstring_parser import parse_from_object

def test_from_class_attribute_docstrings_without_type():
    """Test the parsing of untyped attribute docstrings."""
    
    class WithoutType:  # pylint: disable=missing-class-docstring
        attr_one = "value"
        """Description for attr_one"""
    
    docstring = parse_from_object(WithoutType)
    
    assert docstring.short_description is None, f"Expected short description to be None, but got {docstring.short_description}"