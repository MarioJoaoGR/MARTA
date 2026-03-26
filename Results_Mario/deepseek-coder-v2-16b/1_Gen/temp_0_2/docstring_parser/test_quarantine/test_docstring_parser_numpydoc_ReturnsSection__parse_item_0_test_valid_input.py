
import pytest
from docstring_parser.numpydoc import ReturnsSection, DocstringReturns

def test_valid_input():
    parser = ReturnsSection()
    key = "return_name : type"
    value = "A description of this returned value"
    
    result = parser._parse_item(key, value)
    
    assert isinstance(result, DocstringReturns)
    assert result.type_name == "type"
    assert result.description == "A description of this returned value"
    assert result.return_name == "return_name"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_ReturnsSection__parse_item_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_ReturnsSection__parse_item_0_test_valid_input.py:6:13: E1120: No value for argument 'title' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_ReturnsSection__parse_item_0_test_valid_input.py:6:13: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)


"""