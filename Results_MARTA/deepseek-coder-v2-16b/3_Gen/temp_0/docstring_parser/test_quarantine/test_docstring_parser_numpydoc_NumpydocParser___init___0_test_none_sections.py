
import pytest
from docstring_parser.numpydoc import NumpydocParser, DEFAULT_SECTIONS, Section

def test_none_sections():
    parser = NumpydocParser()
    assert isinstance(parser.sections, dict)
    assert len(parser.sections) == len(DEFAULT_SECTIONS)
    for section in DEFAULT_SECTIONS.values():
        assert section.title in parser.sections

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_NumpydocParser___init___0_test_none_sections
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser___init___0_test_none_sections.py:9:19: E1101: Instance of 'list' has no 'values' member (no-member)


"""