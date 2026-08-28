
import pytest
from unittest.mock import patch, MagicMock
from googleparser import GoogleParser, Section
from docstring_parser.google import DocstringMeta, DocstringParam, DocstringReturns, DocstringRaises

# Test for initializing GoogleParser with default sections and requiring title colons
def test_GoogleParser_default_init():
    parser = GoogleParser()
    assert hasattr(parser, 'sections')
    assert isinstance(parser.sections, dict)
    assert parser.title_colon is True

# Test for initializing GoogleParser with custom sections and not requiring title colons
def test_GoogleParser_custom_init():
    custom_sections = [Section('Title1', 'key1'), Section('Title2', 'key2')]
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    assert hasattr(parser, 'sections')
    assert isinstance(parser.sections, dict)
    assert parser.title_colon is False

# Test for parsing a docstring with default settings
def test_parse_docstring_default():
    docstring_text = "Short description.\n\nLong description.\nSection title:\nContent under section."
    parsed_docstring = GoogleParser().parse(docstring_text)
    assert hasattr(parsed_docstring, 'short_description')
    assert hasattr(parsed_docstring, 'long_description')
    assert hasattr(parsed_docstring, 'meta')
    assert isinstance(parsed_docstring.meta, list)

# Test for parsing a docstring with custom sections and not requiring title colons
def test_parse_docstring_custom():
    custom_sections = [Section('Title1', 'key1'), Section('Title2', 'key2')]
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    docstring_text = "Short description.\n\nLong description.\nTitle1:\nContent under Title1.\nTitle2:\nContent under Title2."
    parsed_docstring = parser.parse(docstring_text)
    assert hasattr(parsed_docstring, 'short_description')
    assert hasattr(parsed_docstring, 'long_description')
    assert hasattr(parsed_docstring, 'meta')
    assert isinstance(parsed_docstring.meta, list)
    assert len(parsed_docstring.meta) == 2

# Test for parsing a docstring with param section
def test_parse_docstring_param():
    custom_sections = [Section('Title1', 'key1')]
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    docstring_text = "Short description.\n\nLong description.\nTitle1: param1, int\nDescription of param1."
    parsed_docstring = parser.parse(docstring_text)
    assert hasattr(parsed_docstring, 'short_description')
    assert hasattr(parsed_docstring, 'long_description')
    assert hasattr(parsed_docstring, 'meta')
    assert isinstance(parsed_docstring.meta, list)
    assert len(parsed_docstring.meta) == 1
    assert parsed_docstring.meta[0].arg_name == 'param1'
    assert parsed_docstring.meta[0].type_name == 'int'
    assert parsed_docstring.meta[0].is_optional is None

# Test for parsing a docstring with returns section
def test_parse_docstring_returns():
    custom_sections = [Section('Title1', 'key1')]
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    docstring_text = "Short description.\n\nLong description.\nTitle1: return, int\nDescription of the return value."
    parsed_docstring = parser.parse(docstring_text)
    assert hasattr(parsed_docstring, 'short_description')
    assert hasattr(parsed_docstring, 'long_description')
    assert hasattr(parsed_docstring, 'meta')
    assert isinstance(parsed_docstring.meta, list)
    assert len(parsed_docstring.meta) == 1
    assert parsed_docstring.meta[0].type_name == 'int'

# Test for parsing a docstring with raises section
def test_parse_docstring_raises():
    custom_sections = [Section('Title1', 'key1')]
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    docstring_text = "Short description.\n\nLong description.\nTitle1: raise, Exception\nDescription of the exception."
    parsed_docstring = parser.parse(docstring_text)
    assert hasattr(parsed_docstring, 'short_description')
    assert hasattr(parsed_docstring, 'long_description')
    assert hasattr(parsed_docstring, 'meta')
    assert isinstance(parsed_docstring.meta, list)
    assert len(parsed_docstring.meta) == 1
    assert parsed_docstring.meta[0].type_name == 'Exception'

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
_ ERROR collecting test_docstring_parser_google_GoogleParser__build_multi_meta_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser__build_multi_meta_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser__build_multi_meta_0.py:4: in <module>
    from googleparser import GoogleParser, Section
E   ModuleNotFoundError: No module named 'googleparser'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser__build_multi_meta_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""