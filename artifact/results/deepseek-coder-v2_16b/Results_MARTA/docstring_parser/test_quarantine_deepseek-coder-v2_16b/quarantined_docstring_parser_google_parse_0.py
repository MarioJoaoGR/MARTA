
import pytest
from docstring_parser.google import parse
from docstring_parser.structures import Docstring

def test_parse_basic():
    """Test parsing a basic Google-style docstring."""
    text = "Short description.\n\nLong description.\nSection title:\nContent under section."
    parsed_docstring = parse(text)
    assert parsed_docstring.short_description == "Short description."
    assert parsed_docstring.long_description == "Long description."
    assert parsed_docstring.meta[0].title == "Section title"
    assert parsed_docstring.meta[0].content == "Content under section."

def test_parse_empty():
    """Test parsing an empty Google-style docstring."""
    text = ""
    parsed_docstring = parse(text)
    assert parsed_docstring.short_description is None
    assert parsed_docstring.long_description is None
    assert len(parsed_docstring.meta) == 0

def test_parse_custom_sections():
    """Test parsing a Google-style docstring with custom sections."""
    text = "Short description.\n\nLong description.\nCustom title:\nContent under custom section."
    parsed_docstring = parse(text)
    assert parsed_docstring.short_description == "Short description."
    assert parsed_docstring.long_description == "Long description."
    assert len(parsed_docstring.meta) == 1
    assert parsed_docstring.meta[0].title == "Custom title"
    assert parsed_docstring.meta[0].content == "Content under custom section."

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
___________ ERROR collecting test_docstring_parser_google_parse_0.py ___________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_parse_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_parse_0.py:4: in <module>
    from docstring_parser.structures import Docstring
E   ModuleNotFoundError: No module named 'docstring_parser.structures'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_google_parse_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""