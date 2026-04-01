
import pytest
from docstring_parser import epydoc

def test_valid_input_clean_style():
    assert process_desc("This is a test.", True) == ' This is a test.'
    assert process_desc("Line one.\nLine two.\nLine three.", False) == 'Line one.\n Line two.\n Line three.'
    assert process_desc(None, False) == ''

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_epydoc_process_desc_0_test_valid_input_clean_style
docstring_parser/Test4DT_tests/test_docstring_parser_epydoc_process_desc_0_test_valid_input_clean_style.py:6:11: E0602: Undefined variable 'process_desc' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_epydoc_process_desc_0_test_valid_input_clean_style.py:7:11: E0602: Undefined variable 'process_desc' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_epydoc_process_desc_0_test_valid_input_clean_style.py:8:11: E0602: Undefined variable 'process_desc' (undefined-variable)


"""