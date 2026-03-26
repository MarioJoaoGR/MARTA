
import pytest
from docstring_parser import parse_from_object

def test_from_class_attribute_docstrings():
    """Test the parsing of attribute docstrings from a class."""

    # Define a class with multiple attributes and their respective docstrings
    class StandardCase:
        """Short description
        Long description"""

        attr_one: str = None
        """Description for attr_one"""
        attr_two: bool = False
        """Description for attr_two"""

    # Parse the class to get the docstring object
    docstring = parse_from_object(StandardCase)

    # Assertions to verify the parsed results
    assert docstring.short_description == "Short description"
    assert docstring.long_description == "Long description"
    assert docstring.description == "Short description\nLong description"
    assert len(docstring.params) == 2
    assert docstring.params[0].arg_name == "attr_one"
    assert docstring.params[0].type_name == "str"
    assert docstring.params[0].description == "Description for attr_one"
    assert docstring.params[1].arg_name == "attr_two"
    assert docstring.params[1].type_name == "bool"
    assert docstring.params[1].description == "Description for attr_two"

# Additional test cases to cover uncovered lines
def test_parse_from_object_missing_docstrings():
    """Test the parsing of attribute docstrings from a class with missing docstrings."""
    
    # Define a class without any docstrings in attributes
    class MissingDocstrings:
        attr_one: str = None
        attr_two: bool = False

    # Parse the class to get the docstring object
    docstring = parse_from_object(MissingDocstrings)

    # Assertions to verify the parsed results
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.description is None
    assert len(docstring.params) == 2
    assert docstring.params[0].arg_name == "attr_one"
    assert docstring.params[0].type_name == "str"
    assert docstring.params[0].description is None
    assert docstring.params[1].arg_name == "attr_two"
    assert docstring.params[1].type_name == "bool"
    assert docstring.params[1].description is None

def test_parse_from_object_empty_docstrings():
    """Test the parsing of attribute docstrings from a class with empty docstrings."""
    
    # Define a class with attributes having empty docstrings
    class EmptyDocstrings:
        attr_one: str = None
        """"""
        attr_two: bool = False
        """"""

    # Parse the class to get the docstring object
    docstring = parse_from_object(EmptyDocstrings)

    # Assertions to verify the parsed results
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.description is None
    assert len(docstring.params) == 2
    assert docstring.params[0].arg_name == "attr_one"
    assert docstring.params[0].type_name == "str"
    assert docstring.params[0].description == ""
    assert docstring.params[1].arg_name == "attr_two"
    assert docstring.params[1].type_name == "bool"
    assert docstring.params[1].description == ""

def test_parse_from_object_multiple_attributes():
    """Test the parsing of attribute docstrings from a class with multiple attributes."""
    
    # Define a class with more than two attributes and their respective docstrings
    class MultipleAttributes(StandardCase):  # Inherit from StandardCase to reuse its structure
        attr_three: int = 0
        """Description for attr_three"""

    # Parse the class to get the docstring object
    docstring = parse_from_object(MultipleAttributes)

    # Assertions to verify the parsed results
    assert docstring.short_description == "Short description"
    assert docstring.long_description == "Long description"
    assert docstring.description == "Short description\nLong description"
    assert len(docstring.params) == 3
    assert docstring.params[0].arg_name == "attr_one"
    assert docstring.params[0].type_name == "str"
    assert docstring.params[0].description == "Description for attr_one"
    assert docstring.params[1].arg_name == "attr_two"
    assert docstring.params[1].type_name == "bool"
    assert docstring.params[1].description == "Description for attr_two"
    assert docstring.params[2].arg_name == "attr_three"
    assert docstring.params[2].type_name == "int"
    assert docstring.params[2].description == "Description for attr_three"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_2
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_2.py:86:29: E0602: Undefined variable 'StandardCase' (undefined-variable)

"""