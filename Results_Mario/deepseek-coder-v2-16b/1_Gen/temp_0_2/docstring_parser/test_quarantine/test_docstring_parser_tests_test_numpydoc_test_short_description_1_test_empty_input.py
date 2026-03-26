
import pytest
from your_module import parse

def test_short_description():
    """Test parsing short description."""
    # Test with empty input
    docstring = parse('')
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert not docstring.meta

    # Test with non-empty but still valid input (should be parsed correctly)
    source = "Example source"
    expected = "Expected short description"
    docstring = parse(source)
    assert docstring.short_description == expected
    assert docstring.long_description is None
    assert not docstring.meta

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_short_description_1_test_empty_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_short_description_1_test_empty_input.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""