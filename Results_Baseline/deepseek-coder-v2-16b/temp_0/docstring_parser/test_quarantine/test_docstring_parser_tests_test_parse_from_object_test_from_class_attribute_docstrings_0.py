
# Module: docstring_parser.tests.test_parse_from_object
# test_parse_from_object.py
import pytest
from docstring_parser import parse_from_object, StandardCase  # Corrected the import statement and added 'StandardCase'

def test_parse_from_class_attribute_docstrings():
    """Test the parsing of attribute docstrings from a class."""
    
    # Create an instance of the StandardCase class for testing
    standard_case = StandardCase()  # Corrected to use the imported 'StandardCase'
    
    # Parse the docstring from the created instance
    docstring = parse_from_object(StandardCase)  # Corrected function call and argument
    
    # Assertions to verify the parsed docstring information
    assert docstring.short_description == "Short description"
    assert docstring.long_description == "Long description"
    assert docstring.description == "Short description\nLong description"
    assert len(docstring.params) == 2
    
    # Check the first attribute (attr_one)
    attr_one_param = docstring.params[0]
    assert attr_one_param.arg_name == "attr_one"
    assert attr_one_param.type_name == "str"
    assert attr_one_param.description == "Description for attr_one"
    
    # Check the second attribute (attr_two)
    attr_two_param = docstring.params[1]
    assert attr_two_param.arg_name == "attr_two"
    assert attr_two_param.type_name == "bool"
    assert attr_two_param.description == "Description for attr_two"

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_0.py:5:0: E0611: No name 'StandardCase' in module 'docstring_parser' (no-name-in-module)

"""