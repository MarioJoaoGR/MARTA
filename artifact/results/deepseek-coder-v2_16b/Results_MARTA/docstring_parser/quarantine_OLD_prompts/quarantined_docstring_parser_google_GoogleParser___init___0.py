
import pytest
from unittest.mock import patch, MagicMock
from googleparser import GoogleParser, Section, DEFAULT_SECTIONS

# Test initialization with custom sections and disabled title colons
def test_custom_sections_disabled_title_colons():
    from googleparser import GoogleParser, Section
    
    # Create custom sections
    custom_sections = [Section('Title1', 'key1'), Section('Title2', 'key2')]

    # Instantiate the parser with custom sections and disable title colons
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    
    assert parser.title_colon == False
    assert len(parser.sections) == 2
    assert 'Title1' in parser.sections
    assert 'Title2' in parser.sections

# Test initialization with default sections and enabled title colons
def test_default_sections_enabled_title_colons():
    from googleparser import GoogleParser
    
    # Instantiate the parser without any specified sections
    parser = GoogleParser()
    
    assert parser.title_colon == True
    assert len(parser.sections) > 0

# Test parsing a docstring with custom sections and disabled title colons
def test_parse_docstring():
    from googleparser import GoogleParser, Section
    
    # Create custom sections
    custom_sections = [Section('Title1', 'key1'), Section('Title2', 'key2')]

    # Instantiate the parser with custom sections and disable title colons
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    
    # Example docstring text
    docstring_text = "Short description.\n\nLong description.\nSection title:\nContent under section."

    # Parse the docstring
    parsed_docstring = parser.parse(docstring_text)
    
    assert len(parsed_docstring.meta) == 2
    assert 'Title1' in parsed_docstring.meta
    assert 'Title2' in parsed_docstring.meta

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
___ ERROR collecting test_docstring_parser_google_GoogleParser___init___0.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser___init___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser___init___0.py:4: in <module>
    from googleparser import GoogleParser, Section, DEFAULT_SECTIONS
E   ModuleNotFoundError: No module named 'googleparser'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser___init___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""