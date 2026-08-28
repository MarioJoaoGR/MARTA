
import pytest
from unittest.mock import patch, MagicMock
from googleparser import GoogleParser, Section, DEFAULT_SECTIONS, RETURNS_KEYWORDS, YIELDS_KEYWORDS, RAISES_KEYWORDS, PARAM_KEYWORDS
from docstring_parser.google import DocstringMeta, ParseError

# Test 1: Default Initialization
def test_default_initialization():
    with patch('googleparser.DEFAULT_SECTIONS', []):
        parser = GoogleParser()
        assert parser.title_colon is True
        assert len(parser.sections) == len(DEFAULT_SECTIONS)

# Test 2: Custom Sections with Title Colons Required
def test_custom_sections_with_title_colons():
    custom_sections = [Section('Title1'), Section('Title2')]
    parser = GoogleParser(sections=custom_sections, title_colon=True)
    assert parser.title_colon is True
    assert len(parser.sections) == 2
    for section in custom_sections:
        assert section.title in parser.sections

# Test 3: Custom Sections without Title Colons
def test_custom_sections_without_title_colons():
    custom_sections = [Section('Title1'), Section('Title2')]
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    assert parser.title_colon is False
    assert len(parser.sections) == 2
    for section in custom_sections:
        assert section.title in parser.sections

# Test 4: Initialization with No Sections (uses default sections)
def test_no_sections():
    with patch('googleparser.DEFAULT_SECTIONS', []):
        parser = GoogleParser(title_colon=True)
        assert parser.title_colon is True
        assert len(parser.sections) == 0

# Test 5: Parse a Docstring with Custom Sections and No Title Colons
def test_parse_docstring_with_custom_sections():
    custom_sections = [Section('Title1'), Section('Title2')]
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    docstring_text = "Short description.\n\nLong description.\nTitle1:\nContent under section 1.\nTitle2:\nContent under section 2."
    parsed_docstring = parser.parse(docstring_text)
    assert len(parsed_docstring.meta) == 2
    for i, meta in enumerate(parsed_docstring.meta):
        if meta.args[0] == 'Title1':
            assert meta.description == "Content under section 1."
        elif meta.args[0] == 'Title2':
            assert meta.description == "Content under section 2."

# Test 6: Parse a Docstring with Invalid Section Key
def test_parse_docstring_with_invalid_section_key():
    custom_sections = [Section('Invalid')]
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    docstring_text = "Short description.\n\nLong description.\nInvalid:\nContent under invalid section."
    with pytest.raises(ParseError):
        parsed_docstring = parser.parse(docstring_text)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_docstring_parser_google_GoogleParser__build_single_meta_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser__build_single_meta_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser__build_single_meta_0.py:4: in <module>
    from googleparser import GoogleParser, Section, DEFAULT_SECTIONS, RETURNS_KEYWORDS, YIELDS_KEYWORDS, RAISES_KEYWORDS, PARAM_KEYWORDS
E   ModuleNotFoundError: No module named 'googleparser'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser__build_single_meta_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""