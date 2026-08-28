
import pytest
from googleparser import GoogleParser, Section
from docstring_parser.google import DEFAULT_SECTIONS, PARAM_KEYWORDS, RETURNS_KEYWORDS, YIELDS_KEYWORDS, RAISES_KEYWORDS
from docstring_parser.models import DocstringMeta, DocstringParam, DocstringReturns, DocstringRaises
import re

# Define regex patterns for testing
GOOGLE_TYPED_ARG_REGEX = re.compile(r"^(\w+)\s*:\s*(.*)$")
GOOGLE_ARG_DESC_REGEX = re.compile(r"^\s*--\s*(.*)")

def test_GoogleParser_default_init():
    parser = GoogleParser()
    assert isinstance(parser, GoogleParser)
    assert parser.title_colon is True
    assert len(parser.sections) == 4
    for section in DEFAULT_SECTIONS:
        assert section.title in parser.sections

def test_GoogleParser_custom_init():
    custom_sections = [Section('Title1', 'key1'), Section('Title2', 'key2')]
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    assert isinstance(parser, GoogleParser)
    assert parser.title_colon is False
    assert len(parser.sections) == 2
    for section in custom_sections:
        assert section.title in parser.sections

def test_GoogleParser__build_multi_meta():
    parser = GoogleParser()
    section = Section('Title', 'key')
    before = "arg_name : type, optional"
    desc = "Description of the argument."
    
    meta = parser._build_multi_meta(section, before, desc)
    
    assert isinstance(meta, DocstringParam)
    assert meta.args == ['Title', 'arg_name']
    assert meta.description == "Description of the argument."
    assert meta.arg_name == "arg_name"
    assert meta.type_name == "type"
    assert meta.is_optional is True

def test_GoogleParser__build_multi_meta_returns():
    parser = GoogleParser()
    section = Section('Returns', 'return')
    before = "ReturnType"
    desc = "Description of the return type."
    
    meta = parser._build_multi_meta(section, before, desc)
    
    assert isinstance(meta, DocstringReturns)
    assert meta.args == ['Returns', 'ReturnType']
    assert meta.description == "Description of the return type."
    assert meta.type_name == "ReturnType"
    assert not meta.is_generator

def test_GoogleParser__build_multi_meta_raises():
    parser = GoogleParser()
    section = Section('Raises', 'raise')
    before = "ExceptionType"
    desc = "Description of the exception."
    
    meta = parser._build_multi_meta(section, before, desc)
    
    assert isinstance(meta, DocstringRaises)
    assert meta.args == ['Raises', 'ExceptionType']
    assert meta.description == "Description of the exception."
    assert meta.type_name == "ExceptionType"

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
/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser__build_multi_meta_0.py:3: in <module>
    from googleparser import GoogleParser, Section
E   ModuleNotFoundError: No module named 'googleparser'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser__build_multi_meta_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""