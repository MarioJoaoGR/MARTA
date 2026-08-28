
import pytest
from googleparser import GoogleParser, Section
from docstring_parser.google import DocstringMeta, ParseError

# Constants for section keys and keywords
RETURNS_KEYWORDS = {"returns"}
YIELDS_KEYWORDS = {"yields"}
RAISES_KEYWORDS = {"raises"}
PARAM_KEYWORDS = {"param", "parameter"}

def test_default_initialization():
    parser = GoogleParser()
    assert hasattr(parser, 'sections')
    assert isinstance(parser.sections, dict)
    assert parser.title_colon is True

def test_custom_sections_with_title_colons_required():
    custom_sections = [Section('Title1'), Section('Title2')]
    parser = GoogleParser(sections=custom_sections, title_colon=True)
    assert hasattr(parser, 'sections')
    assert isinstance(parser.sections, dict)
    assert parser.title_colon is True

def test_custom_sections_without_title_colons():
    custom_sections = [Section('Title1'), Section('Title2')]
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    assert hasattr(parser, 'sections')
    assert isinstance(parser.sections, dict)
    assert parser.title_colon is False

def test_initialization_with_no_sections():
    parser = GoogleParser(title_colon=True)
    assert hasattr(parser, 'sections')
    assert isinstance(parser.sections, dict)
    assert parser.title_colon is True

def test_build_single_meta_returns():
    section = Section('returns', '')
    desc = "Return description."
    meta = GoogleParser()._build_single_meta(section, desc)
    assert isinstance(meta, DocstringMeta)
    assert meta.args == ['returns']
    assert meta.description == 'Return description.'
    assert meta.type_name is None
    assert not meta.is_generator

def test_build_single_meta_raises():
    section = Section('raises', '')
    desc = "Raise description."
    meta = GoogleParser()._build_single_meta(section, desc)
    assert isinstance(meta, DocstringRaises)
    assert meta.args == ['raises']
    assert meta.description == 'Raise description.'
    assert meta.type_name is None

def test_build_single_meta_param():
    section = Section('parameter', '')
    with pytest.raises(ParseError):
        GoogleParser()._build_single_meta(section, "Parameter description.")

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
/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser__build_single_meta_0.py:3: in <module>
    from googleparser import GoogleParser, Section
E   ModuleNotFoundError: No module named 'googleparser'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser__build_single_meta_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""