
import pytest
from docstring_parser.numpydoc import NumpydocParser, Section, DEFAULT_SECTIONS

def test_valid_sections():
    # Define custom sections
    custom_sections = {
        'Parameters': Section(title='Parameters', title_pattern=r'^Parameters$'),
        'Returns': Section(title='Returns', title_pattern=r'^Returns$')
    }

    # Initialize the parser with custom sections
    parser = NumpydocParser(sections=custom_sections)

    # Check if the sections are correctly set up in the parser
    assert parser.sections == {
        'Parameters': Section(title='Parameters', title_pattern=r'^Parameters$'),
        'Returns': Section(title='Returns', title_pattern=r'^Returns$')
    }

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_NumpydocParser___init___0_test_valid_sections
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser___init___0_test_valid_sections.py:8:22: E1123: Unexpected keyword argument 'title_pattern' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser___init___0_test_valid_sections.py:8:22: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser___init___0_test_valid_sections.py:9:19: E1123: Unexpected keyword argument 'title_pattern' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser___init___0_test_valid_sections.py:9:19: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser___init___0_test_valid_sections.py:17:22: E1123: Unexpected keyword argument 'title_pattern' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser___init___0_test_valid_sections.py:17:22: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser___init___0_test_valid_sections.py:18:19: E1123: Unexpected keyword argument 'title_pattern' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser___init___0_test_valid_sections.py:18:19: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)

"""