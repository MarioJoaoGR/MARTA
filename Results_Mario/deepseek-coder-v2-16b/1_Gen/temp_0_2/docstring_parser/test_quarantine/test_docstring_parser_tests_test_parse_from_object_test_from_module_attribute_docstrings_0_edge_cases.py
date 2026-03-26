
import pytest
from docstring_parser.tests import test_parse_from_object  # pylint: disable=C0415,W0406

def test_from_module_attribute_docstrings():
    """Test the parse of attribute docstrings from a module."""
    from . import test_parse_from_object  # pylint: disable=C0415,W0406

    docstring = test_parse_from_object.parse_from_object(test_parse_from_object)

    assert "parse_from_object" in docstring.short_description
    assert len(docstring.params) == 1
    assert docstring.params[0].arg_name == "module_attr"
    assert docstring.params[0].type_name == "int"
    assert docstring.params[0].description == "Description for module_attr"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_parse_from_object_test_from_module_attribute_docstrings_0_edge_cases
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_module_attribute_docstrings_0_edge_cases.py:7:4: E0611: No name 'test_parse_from_object' in module 'Test4DT_tests' (no-name-in-module)


"""