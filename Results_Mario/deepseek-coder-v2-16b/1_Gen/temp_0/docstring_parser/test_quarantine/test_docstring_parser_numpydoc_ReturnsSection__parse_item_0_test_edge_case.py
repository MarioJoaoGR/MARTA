
import pytest
from docstring_parser.numpydoc import DocstringReturns, ReturnsSection

@pytest.fixture
def returns_section():
    return ReturnsSection()

def test_parse_item_with_key(returns_section):
    result = returns_section._parse_item("result : int", "The result of the computation.")
    assert isinstance(result, DocstringReturns)
    assert result.args == ['result']
    assert result.description == 'The result of the computation.'
    assert result.type_name == 'int'
    assert not result.is_generator
    assert result.return_name == 'result'

def test_parse_item_without_key(returns_section):
    result = returns_section._parse_item("another_type", "A generic return value without a specific name.")
    assert isinstance(result, DocstringReturns)
    assert result.args == []
    assert result.description == 'A generic return value without a specific name.'
    assert result.type_name is None
    assert not result.is_generator
    assert result.return_name is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_ReturnsSection__parse_item_0_test_edge_case
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_ReturnsSection__parse_item_0_test_edge_case.py:7:11: E1120: No value for argument 'title' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_ReturnsSection__parse_item_0_test_edge_case.py:7:11: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)

"""