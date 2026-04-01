
import pytest
from docstring_parser.numpydoc import ReturnsSection, DocstringReturns

@pytest.fixture
def returns_section():
    return ReturnsSection()

def test_valid_input(returns_section):
    # Test with a key that includes both name and type
    result = returns_section._parse_item("result : int", "This function returns an integer.")
    assert isinstance(result, DocstringReturns)
    assert result.return_name == "result"
    assert result.type_name == "int"
    assert result.description == "This function returns an integer."

    # Test with a key that only includes type
    another_result = returns_section._parse_item("int", "This section does not specify a name.")
    assert isinstance(another_result, DocstringReturns)
    assert result.return_name is None
    assert another_result.type_name == "int"
    assert another_result.description == "This section does not specify a name."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_ReturnsSection__parse_item_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_ReturnsSection__parse_item_0_test_valid_input.py:7:11: E1120: No value for argument 'title' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_ReturnsSection__parse_item_0_test_valid_input.py:7:11: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)


"""