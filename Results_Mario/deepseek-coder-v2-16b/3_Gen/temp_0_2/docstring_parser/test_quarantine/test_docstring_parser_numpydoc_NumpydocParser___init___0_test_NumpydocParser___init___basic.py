
import pytest
from docstring_parser.numpydoc import NumpydocParser, Section, DEFAULT_SECTIONS

def test_NumpydocParser___init___basic():
    # Test default initialization with no sections provided
    parser = NumpydocParser()
    assert isinstance(parser.sections, dict)
    assert len(parser.sections) == len(DEFAULT_SECTIONS)
    
    # Test initialization with custom sections provided
    custom_sections = {
        'Parameters': Section(title='Parameters', title_pattern=r'^\s*Parameters\b'),
        'Returns': Section(title='Returns', title_pattern=r'^\s*Returns\b')
    }
    parser = NumpydocParser(sections=custom_sections)
    assert isinstance(parser.sections, dict)
    assert len(parser.sections) == 2
    assert 'Parameters' in parser.sections
    assert 'Returns' in parser.sections

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_NumpydocParser___init___0_test_NumpydocParser___init___basic
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser___init___0_test_NumpydocParser___init___basic.py:13:22: E1123: Unexpected keyword argument 'title_pattern' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser___init___0_test_NumpydocParser___init___basic.py:13:22: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser___init___0_test_NumpydocParser___init___basic.py:14:19: E1123: Unexpected keyword argument 'title_pattern' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser___init___0_test_NumpydocParser___init___basic.py:14:19: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)


"""