
import pytest
from docstring_parser.numpydoc import Section

def test_valid_input():
    section = Section(title="Parameters", key="params")
    
    assert section.title == "Parameters"
    assert section.key == "params"
    
    # Test the title pattern method
    expected_pattern = rf"^({section.title})\s*?\n{'-' * len(section.title)}\s*$"
    assert section.title_pattern() == expected_pattern

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_Section_title_pattern_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_Section_title_pattern_0_test_valid_input.py:13:11: E1102: section.title_pattern is not callable (not-callable)


"""