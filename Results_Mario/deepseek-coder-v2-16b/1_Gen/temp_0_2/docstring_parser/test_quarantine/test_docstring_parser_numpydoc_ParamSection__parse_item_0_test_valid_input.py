
import pytest
from docstring_parser.numpydoc import ParamSection, DocstringParam

def test_valid_input():
    parser = ParamSection()
    param_metadata = parser._parse_item(key='example_param', value='int, optional')
    
    assert isinstance(param_metadata, DocstringParam)
    assert param_metadata.arg_name == 'example_param'
    assert param_metadata.type_name == 'int'
    assert param_metadata.is_optional is True
    assert param_metadata.default is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_ParamSection__parse_item_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_ParamSection__parse_item_0_test_valid_input.py:6:13: E1120: No value for argument 'title' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_ParamSection__parse_item_0_test_valid_input.py:6:13: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)


"""