
from docstring_parser.numpydoc import DocstringRaises
from docstring_parser.numpydoc import RaisesSection as RS

def test_valid_input():
    parser = RS()
    parsed_section = parser._parse_item(key="ValueError", value="A description of what might raise ValueError")
    
    assert isinstance(parsed_section, DocstringRaises)
    assert parsed_section.args == ["ValueError"]
    assert parsed_section.description == "A description of what might raise ValueError"
    assert parsed_section.type_name == "ValueError"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_RaisesSection__parse_item_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_RaisesSection__parse_item_0_test_valid_input.py:6:13: E1120: No value for argument 'title' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_RaisesSection__parse_item_0_test_valid_input.py:6:13: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)


"""