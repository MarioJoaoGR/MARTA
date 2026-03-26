
import pytest
from .your_module import Docstring, parse

@pytest.mark.parametrize("docstring, expected_short_desc, expected_long_desc, expected_blank", [
    ("", "", "", False),
    ("   ", "", "", False),
    (None, None, None, True),
    ("Short description\n\nLong description", "Short description", "Long description", True),
    ("Short description", "Short description", "", False),
    ("", "", "", False),
])
def test_long_description(docstring, expected_short_desc, expected_long_desc, expected_blank):
    docstring = parse(docstring)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_long_description_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_long_description_0.py:3:0: E0401: Unable to import 'Test4DT_tests.your_module' (import-error)

"""