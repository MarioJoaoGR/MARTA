
# Module: docstring_parser.tests.test_rest
import pytest
from numpydoc_parser import parse

# Test cases for the test_long_description function
@pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank", [
    (
        "This is a short description.\n\nExtended description with details.",
        "This is a short description.",
        "Extended description with details.",
        True
    ),
    (
        "Short desc only.",
        "Short desc only.",
        "",
        False
    ),
    (
        "\n\nNo content here.\n\n",
        "",
        "",
        False
    ),
    (
        "A short description with a newline.\nExtended long description.",
        "A short description with a newline.",
        "Extended long description.",
        True
    )
])
def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank
    assert not docstring.meta

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_rest_test_long_description_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0.py:4:0: E0401: Unable to import 'numpydoc_parser' (import-error)

"""