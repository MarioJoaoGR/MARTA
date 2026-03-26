
import pytest
from docstring_parser.numpydoc import DeprecationSection, DocstringDeprecated

def test_empty_input():
    parser = DeprecationSection()
    deprecations = list(parser.parse(""))
    
    assert len(deprecations) == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_DeprecationSection_parse_0_test_empty_input
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_DeprecationSection_parse_0_test_empty_input.py:6:13: E1120: No value for argument 'title' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_DeprecationSection_parse_0_test_empty_input.py:6:13: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)


"""