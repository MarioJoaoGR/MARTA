
import pytest
from docstring_parser.common import Docstring, DocstringStyle

def test_edge_case_none():
    # Test that a Docstring object can be created with None as the style parameter
    docstring_obj = Docstring(style=None)
    
    # Check if the style attribute is set to None
    assert docstring_obj.style is None
