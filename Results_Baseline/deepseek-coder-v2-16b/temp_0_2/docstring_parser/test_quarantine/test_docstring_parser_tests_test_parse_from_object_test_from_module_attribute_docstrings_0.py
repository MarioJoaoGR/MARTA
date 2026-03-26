
# Module: docstring_parser.tests.test_parse_from_object
# test_parse_from_object.py
import pytest
from . import test_parse_from_object  # pylint: disable=C0415,W0406
from docstring_parser import parse_from_object

def test_from_module_attribute_docstrings():
    """Test the parsing of attribute docstrings from a module."""
    
    docstring = parse_from_object(test_parse_from_object)

    assert "parse_from_object" in docstring.short_description, f"Expected 'parse_from_object' in short description but got {docstring.short_description}"
    assert len(docstring.params) == 1, f"Expected one parameter but got {len(docstring.params)}"
    assert docstring.params[0].arg_name == "module_attr", f"Expected parameter name 'module_attr' but got {docstring.params[0].arg_name}"
    assert docstring.params[0].type_name == "int", f"Expected type 'int' for parameter 'module_attr' but got {docstring.params[0].type_name}"
    assert docstring.params[0].description == "Description for module_attr", f"Expected description 'Description for module_attr' for parameter 'module_attr' but got {docstring.params[0].description}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_parse_from_object_test_from_module_attribute_docstrings_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_module_attribute_docstrings_0.py:5:0: E0611: No name 'test_parse_from_object' in module 'Test4DT_tests' (no-name-in-module)

"""