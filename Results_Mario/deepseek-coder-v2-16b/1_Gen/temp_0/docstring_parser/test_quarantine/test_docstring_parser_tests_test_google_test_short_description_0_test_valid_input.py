
import pytest
from docstring_parser.tests.test_google import parse, test_short_description

@pytest.fixture(params=[("This is a summary.", "This is a summary."), ("", None)])
def source_expected_pairs(request):
    return request.param

def test_short_description(source_expected_pairs):
    source, expected = source_expected_pairs
    docstring = parse(source)
    assert docstring.short_description == expected
    assert docstring.long_description is None
    assert not docstring.meta

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_short_description_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_valid_input.py:9:0: E0102: function already defined line 3 (function-redefined)

"""