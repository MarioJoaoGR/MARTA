
# Module: docstring_parser.tests.test_parse_from_object
import pytest
from unittest.mock import patch
from your_module_name import parse_from_object, WithoutSource

def test_from_class_without_source():
    """Test the parse of class when source is unavailable."""
    
    class WithoutSource:
        """Short description"""
        
        attr_one: str
        """Description for attr_one"""
    
    with patch(
        "inspect.getsource", side_effect=OSError("could not get source code")
    ):
        docstring = parse_from_object(WithoutSource)
    
    assert docstring.short_description == "Short description"
    assert docstring.long_description is None
    assert docstring.description == "Short description"
    assert len(docstring.params) == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_parse_from_object_test_from_class_without_source_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_without_source_0.py:5:0: E0401: Unable to import 'your_module_name' (import-error)

"""