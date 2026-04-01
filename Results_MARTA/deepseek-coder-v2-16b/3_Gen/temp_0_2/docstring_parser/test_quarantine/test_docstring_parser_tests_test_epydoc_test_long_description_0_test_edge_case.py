
from docstring_parser import parse
import pytest

@pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank", [
    ("This is a test.\n\n@param arg1: Description of argument 1.\n@return: Result of the operation.", "This is a test.", "Description of argument 1.\nResult of the operation.", True)
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
************* Module Test4DT_tests.test_docstring_parser_tests_test_epydoc_test_long_description_0_test_edge_case
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_long_description_0_test_edge_case.py:2:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""