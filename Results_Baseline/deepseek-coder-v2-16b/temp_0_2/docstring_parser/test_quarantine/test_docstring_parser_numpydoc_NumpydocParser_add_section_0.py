
# Module: docstring_parser.numpydoc
import pytest
from numpypy_parser import NumpydocParser, Section, DEFAULT_SECTIONS

# Test initialization with default sections
def test_init_with_default_sections():
    parser = NumpydocParser()
    assert isinstance(parser.sections, dict)
    assert len(parser.sections) == len(DEFAULT_SECTIONS)

# Test initialization with custom sections
def test_init_with_custom_sections():
    custom_sections = {
        'Parameters': Section(title='Parameters', title_pattern=r'\bParameters\b'),
        'Returns': Section(title='Returns', title_pattern=r'\bReturns\b')
    }
    parser = NumpydocParser(sections=custom_sections)
    assert isinstance(parser.sections, dict)
    assert len(parser.sections) == len(custom_sections)

# Test adding a new section
def test_add_new_section():
    custom_sections = {
        'Parameters': Section(title='Parameters', title_pattern=r'\bParameters\b')
    }
    parser = NumpydocParser(sections=custom_sections)
    assert 'Example' not in parser.sections
    
    new_section = Section(title='Example', title_pattern=r'\bExample\b')
    parser.add_section(new_section)
    assert 'Example' in parser.sections

# Test replacing an existing section
def test_replace_existing_section():
    custom_sections = {
        'Parameters': Section(title='Parameters', title_pattern=r'\bParameters\b')
    }
    parser = NumpydocParser(sections=custom_sections)
    
    updated_section = Section(title='Parameters', title_pattern=r'\bParameters\b')
    parser.add_section(updated_section)
    assert len(parser.sections) == len(custom_sections)
    assert parser.sections['Parameters'].title == 'Parameters'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_NumpydocParser_add_section_0
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser_add_section_0.py:4:0: E0401: Unable to import 'numpypy_parser' (import-error)

"""