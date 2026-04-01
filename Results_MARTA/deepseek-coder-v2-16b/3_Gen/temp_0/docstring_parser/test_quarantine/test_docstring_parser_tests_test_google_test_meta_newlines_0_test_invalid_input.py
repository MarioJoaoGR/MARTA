
import pytest
from docstring_parser.tests.test_google import parse, test_meta_newlines

@pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc", [
    (
        "This is a summary.\n\nArgs:\nparam1 (int): Description of parameter 1.\nparam2 (str): Description of parameter 2.\n\nReturns:\n    int: The result of the operation, which could be an integer.",
        "This is a summary.",
        "Args:\nparam1 (int): Description of parameter 1.\nparam2 (str): Description of parameter 2.\n\nReturns:\n    int: The result of the operation, which could be an integer.",
        True,
        True
    )
])
def test_meta_newlines(source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc):
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank_short_desc
    assert docstring.blank_after_long_description == expected_blank_long_desc
    assert len(docstring.meta) == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_meta_newlines_0_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_meta_newlines_0_test_invalid_input.py:14:0: E0102: function already defined line 3 (function-redefined)


"""