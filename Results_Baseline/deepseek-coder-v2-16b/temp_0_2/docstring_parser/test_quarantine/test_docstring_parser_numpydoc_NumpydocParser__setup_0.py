
# Module: docstring_parser.numpydoc
import pytest
from numpydoc_parser import NumpydocParser, DEFAULT_SECTIONS
import re

# Test initialization with custom sections
def test_init_with_custom_sections():
    from numpydoc_parser import Section
    custom_sections = {
        'Parameters': Section(title='Parameters', title_pattern=r'\bParameters\b'),
        'Returns': Section(title='Returns', title_pattern=r'\bReturns\b')
    }
    parser = NumpydocParser(sections=custom_sections)
    assert parser.sections == custom_sections

# Test initialization with default sections
def test_init_with_default_sections():
    from numpydoc_parser import NumpydocParser
    parser = NumpydocParser()
    assert parser.sections == DEFAULT_SECTIONS

# Test parsing a docstring
def test_parse_docstring():
    from numpydoc_parser import NumpydocParser, Section, DEFAULT_SECTIONS

    custom_sections = {
        'Parameters': Section(title='Parameters', title_pattern=r'\bParameters\b'),
        'Returns': Section(title='Returns', title_pattern=r'\bReturns\b')
    }
    parser = NumpydocParser(sections=custom_sections)
    
    docstring = """
    A short description.
    
    Long description that spans multiple lines.
    
    Parameters:
        param1 (type): Description of param1.
        param2 (type): Description of param2.
        
    Returns:
        type: Description of the return value.
    """
    parsed_docstring = parser.parse(docstring)
    assert isinstance(parsed_docstring, dict)
    assert 'Parameters' in parsed_docstring
    assert 'Returns' in parsed_docstring

# Test adding a new section
def test_add_section():
    from numpydoc_parser import NumpydocParser, Section, DEFAULT_SECTIONS

    custom_sections = {
        'Parameters': Section(title='Parameters', title_pattern=r'\bParameters\b'),
        'Returns': Section(title='Returns', title_pattern=r'\bReturns\b')
    }
    parser = NumpydocParser(sections=custom_sections)
    
    new_section = Section(title='Example', title_pattern=r'\bExample\b')
    parser.add_section(new_section)
    assert 'Example' in parser.sections

# Test setup method
def test_setup():
    from numpydoc_parser import NumpydocParser, Section
    custom_sections = {
        'Parameters': Section(title='Parameters', title_pattern=r'\bParameters\b'),
        'Returns': Section(title='Returns', title_pattern=r'\bReturns\b')
    }
    parser = NumpydocParser(sections=custom_sections)
    
    assert re.compile(
        r"|".join(s.title_pattern for s in custom_sections.values()),
        flags=re.M,
    ) == parser.titles_re

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_NumpydocParser__setup_0
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser__setup_0.py:4:0: E0401: Unable to import 'numpydoc_parser' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser__setup_0.py:9:4: E0401: Unable to import 'numpydoc_parser' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser__setup_0.py:19:4: E0401: Unable to import 'numpydoc_parser' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser__setup_0.py:25:4: E0401: Unable to import 'numpydoc_parser' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser__setup_0.py:52:4: E0401: Unable to import 'numpydoc_parser' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser__setup_0.py:66:4: E0401: Unable to import 'numpydoc_parser' (import-error)

"""