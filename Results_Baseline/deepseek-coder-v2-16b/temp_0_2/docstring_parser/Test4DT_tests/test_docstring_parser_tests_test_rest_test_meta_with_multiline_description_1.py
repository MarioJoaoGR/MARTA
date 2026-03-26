
import pytest
from docstring_parser import parse

def test_meta_with_multiline_description():
    """Test parsing multiline meta documentation."""
    # Test case 1: Basic multi-line meta description
    docstring = parse(
        """
        Short description
    
        :meta: asd
            1
                2
            3
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    meta_entry = docstring.meta[0]
    assert meta_entry.args == ["meta"]
    assert meta_entry.description == "asd\n1\n    2\n3"

    # Test case 2: Meta description with different indentation and spacing
    docstring = parse(
        """
        Another short description
    
        :meta: example
            multiline
                content
                 here
        """
    )
    assert docstring.short_description == "Another short description"
    assert len(docstring.meta) == 1
    meta_entry = docstring.meta[0]
    assert meta_entry.args == ["meta"]