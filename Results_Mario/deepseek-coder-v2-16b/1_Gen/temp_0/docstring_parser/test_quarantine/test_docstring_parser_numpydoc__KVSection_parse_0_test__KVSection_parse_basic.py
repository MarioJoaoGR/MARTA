
import pytest
from docstring_parser.numpydoc import _KVSection

def test__KVSection_parse_basic():
    parser = _KVSection()
    text = "Parameters:\n  arg1 : int\n  arg2 : str"
    
    parsed_sections = list(parser.parse(text))
    
    assert len(parsed_sections) == 2
    
    # Check the first section
    first_section = parsed_sections[0]
    assert isinstance(first_section, DocstringMeta)
    assert first_section.key == 'arg1'
    assert first_section.value == 'int'
    
    # Check the second section
    second_section = parsed_sections[1]
    assert isinstance(second_section, DocstringMeta)
    assert second_section.key == 'arg2'
    assert second_section.value == 'str'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc__KVSection_parse_0_test__KVSection_parse_basic
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc__KVSection_parse_0_test__KVSection_parse_basic.py:6:13: E1120: No value for argument 'title' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc__KVSection_parse_0_test__KVSection_parse_basic.py:6:13: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc__KVSection_parse_0_test__KVSection_parse_basic.py:15:37: E0602: Undefined variable 'DocstringMeta' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc__KVSection_parse_0_test__KVSection_parse_basic.py:21:38: E0602: Undefined variable 'DocstringMeta' (undefined-variable)

"""