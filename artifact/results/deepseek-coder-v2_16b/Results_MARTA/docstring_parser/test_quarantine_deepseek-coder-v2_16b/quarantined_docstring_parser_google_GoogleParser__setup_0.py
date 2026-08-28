
import pytest
from googleparser import GoogleParser, Section
import re

# Test 1: Default Sections with Title Colons
def test_default_sections_with_title_colons():
    parser = GoogleParser()
    docstring_text = "Short description.\n\nLong description.\nSection title:\nContent under section."
    parsed_docstring = parser.parse(docstring_text)
    
    assert parsed_docstring.short_description == "Short description."
    assert parsed_docstring.long_description == "Long description."
    assert len(parsed_docstring.meta) == 1
    assert parsed_docstring.meta[0].key == "Section title"
    assert parsed_docstring.meta[0].value == "Content under section."

# Test 2: Custom Sections without Title Colons
def test_custom_sections_without_title_colons():
    custom_sections = [Section('Title1', 'key1'), Section('Title2', 'key2')]
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    docstring_text = "Short description.\n\nLong description.\nTitle1:\nContent under section 1.\nTitle2:\nContent under section 2."
    parsed_docstring = parser.parse(docstring_text)
    
    assert parsed_docstring.short_description == "Short description."
    assert parsed_docstring.long_description == "Long description."
    assert len(parsed_docstring.meta) == 2
    assert parsed_docstring.meta[0].key == "Title1"
    assert parsed_docstring.meta[0].value == "Content under section 1."
    assert parsed_docstring.meta[1].key == "Title2"
    assert parsed_docstring.meta[1].value == "Content under section 2."

# Test 3: Custom Sections with Title Colons
def test_custom_sections_with_title_colons():
    custom_sections = [Section('Title1', 'key1'), Section('Title2', 'key2')]
    parser = GoogleParser(sections=custom_sections)
    docstring_text = "Short description.\n\nLong description.\nTitle1:\nContent under section 1.\nTitle2:\nContent under section 2."
    parsed_docstring = parser.parse(docstring_text)
    
    assert parsed_docstring.short_description == "Short description."
    assert parsed_docstring.long_description == "Long description."
    assert len(parsed_docstring.meta) == 2
    assert parsed_docstring.meta[0].key == "Title1"
    assert parsed_docstring.meta[0].value == "Content under section 1."
    assert parsed_docstring.meta[1].key == "Title2"
    assert parsed_docstring.meta[1].value == "Content under section 2."

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
____ ERROR collecting test_docstring_parser_google_GoogleParser__setup_0.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser__setup_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser__setup_0.py:3: in <module>
    from googleparser import GoogleParser, Section
E   ModuleNotFoundError: No module named 'googleparser'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_GoogleParser__setup_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""