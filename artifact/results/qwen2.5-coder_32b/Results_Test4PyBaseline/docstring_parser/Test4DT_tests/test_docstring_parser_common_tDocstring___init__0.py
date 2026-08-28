# Module: docstring_parser.common
import pytest
from docstring_parser.common import Docstring

def test_docstring_initialization():
    """Test the initialization of the Docstring class."""
    doc = Docstring()
    
    assert doc.short_description is None, "short_description should be initialized to None"
    assert doc.long_description is None, "long_description should be initialized to None"
    assert not doc.blank_after_short_description, "blank_after_short_description should be False by default"
    assert not doc.blank_after_long_description, "blank_after_long_description should be False by default"
    assert isinstance(doc.meta, list), "meta should be an empty list by default"
    assert len(doc.meta) == 0, "meta list should be empty after initialization"

def test_docstring_attributes_assignment():
    """Test the assignment of attributes in the Docstring class."""
    doc = Docstring()
    
    doc.short_description = "This function adds two numbers."
    doc.long_description = "The function takes two numeric inputs and returns their sum."
    doc.blank_after_short_description = True
    doc.blank_after_long_description = True
    
    assert doc.short_description == "This function adds two numbers.", "short_description should match the assigned value"
    assert doc.long_description == "The function takes two numeric inputs and returns their sum.", "long_description should match the assigned value"
    assert doc.blank_after_short_description, "blank_after_short_description should be True after assignment"
    assert doc.blank_after_long_description, "blank_after_long_description should be True after assignment"

def test_docstring_meta_assignment():
    """Test the addition of metadata to the Docstring class."""
    from typing import List

    class DocstringParam:
        def __init__(self, name: str, type_: str, description: str):
            self.name = name
            self.type_ = type_
            self.description = description

    class DocstringRaises:
        def __init__(self, exception_type: str, description: str):
            self.exception_type = exception_type
            self.description = description

    class DocstringReturns:
        def __init__(self, type_: str, description: str):
            self.type_ = type_
            self.description = description

    doc = Docstring()
    
    param1 = DocstringParam(name="x", type_="int", description="First number")
    param2 = DocstringParam(name="y", type_="int", description="Second number")
    raises_info = DocstringRaises(exception_type="ValueError", description="Raised if inputs are negative.")
    returns_info = DocstringReturns(type_="int", description="Sum of x and y")

    doc.meta.extend([param1, param2, raises_info, returns_info])
    
    assert len(doc.meta) == 4, "meta list should contain 4 items after assignment"
    assert isinstance(doc.meta[0], DocstringParam), "First item in meta should be a DocstringParam instance"
    assert isinstance(doc.meta[1], DocstringParam), "Second item in meta should be a DocstringParam instance"
    assert isinstance(doc.meta[2], DocstringRaises), "Third item in meta should be a DocstringRaises instance"
    assert isinstance(doc.meta[3], DocstringReturns), "Fourth item in meta should be a DocstringReturns instance"

def test_docstring_initialization_with_no_arguments():
    """Test the initialization of the Docstring class with no arguments."""
    doc = Docstring()
    
    assert doc.short_description is None, "short_description should be initialized to None"
    assert doc.long_description is None, "long_description should be initialized to None"
    assert not doc.blank_after_short_description, "blank_after_short_description should be False by default"
    assert not doc.blank_after_long_description, "blank_after_long_description should be False by default"
    assert isinstance(doc.meta, list), "meta should be an empty list by default"
    assert len(doc.meta) == 0, "meta list should be empty after initialization"

def test_docstring_initialization_with_default_values():
    """Test the initialization of the Docstring class with default values."""
    doc = Docstring()
    
    assert doc.short_description is None, "short_description should be initialized to None"
    assert doc.long_description is None, "long_description should be initialized to None"
    assert not doc.blank_after_short_description, "blank_after_short_description should be False by default"
    assert not doc.blank_after_long_description, "blank_after_long_description should be False by default"
    assert isinstance(doc.meta, list), "meta should be an empty list by default"
    assert len(doc.meta) == 0, "meta list should be empty after initialization"
