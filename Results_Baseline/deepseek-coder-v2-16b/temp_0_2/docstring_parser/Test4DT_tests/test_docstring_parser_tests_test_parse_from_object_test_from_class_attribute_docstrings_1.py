
import pytest
from docstring_parser import parse_from_object

def test_parse_from_object_empty_docstring():
    """Test parsing a class with an empty docstring."""
    class EmptyDocstring:
        """"""

        attr_one: str
        """Description for attr_one"""
        attr_two: bool = False
        """Description for attr_two"""

    docstring = parse_from_object(EmptyDocstring)
    assert docstring.short_description is None
    assert docstring.long_description is None