
# Module: docstring_parser.tests.test_parse_from_object
# Import the function correctly using its module name.
from unittest.mock import patch
from your_module import parse_from_object, WithoutSource

def test_from_class_without_source() -> None:
    """Test the parse of class when source is unavailable."""
    
    # Define a mock class with a docstring for testing.
    class WithoutSource:
        """Short description"""
        
        attr_one: str
        """Description for attr_one"""
    
    # Mock inspect.getsource to raise an OSError when called.
    with patch("inspect.getsource", side_effect=OSError("could not get source code")):
        docstring = parse_from_object(WithoutSource)
        
    # Assertions to verify the parsed docstring information.
    assert docstring.short_description == "Short description"
    assert docstring.long_description is None
    assert docstring.description == "Short description"
    assert len(docstring.params) == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_parse_from_object_test_from_class_without_source_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_without_source_0.py:5:0: E0401: Unable to import 'your_module' (import-error)

"""