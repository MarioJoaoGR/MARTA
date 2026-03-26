
import pytest
from docstring_parser.numpydoc import DeprecationSection, DocstringDeprecated

def test_valid_input():
    parser = DeprecationSection()
    text = "1.0\nThis argument is no longer used."
    deprecations = list(parser.parse(text))
    
    assert len(deprecations) == 1
    deprecation = deprecations[0]
    assert isinstance(deprecation, DocstringDeprecated)
    assert deprecation.args == [parser.key]
    assert deprecation.description == "This argument is no longer used."
    assert deprecation.version == "1.0"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_DeprecationSection_parse_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_DeprecationSection_parse_0_test_valid_input.py:6:13: E1120: No value for argument 'title' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_DeprecationSection_parse_0_test_valid_input.py:6:13: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)


"""