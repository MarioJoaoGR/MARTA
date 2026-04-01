
import pytest
from docstring_parser import parse_from_object

def test_from_class_attribute_docstrings_without_type() -> None:
    """Test the parsing of untyped attribute docstrings."""

    class WithoutType:  # pylint: disable=missing-class-docstring
        attr_one = "value"
        """Description for attr_one"""

    docstring = parse_from_object(WithoutType)

    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.description is None
    assert len(docstring.params) == 1
    assert docstring.params[0].arg_name == "attr_one"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "Description for attr_one"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_0_test_test_from_class_attribute_docstrings_without_type_basic
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_0_test_test_from_class_attribute_docstrings_without_type_basic.py:3:0: E0611: No name 'parse_from_object' in module 'docstring_parser' (no-name-in-module)


"""