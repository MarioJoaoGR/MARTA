
import pytest
from docstring_parser.parser import DocstringParser, Style, STYLES, ParseError

def test_parse_default_style():
    """Test parsing a docstring with default style auto-detection."""
    parsed = parse("function description")
    assert isinstance(parsed, Docstring)

def test_parse_specific_style():
    """Test parsing a docstring with a specific style."""
    parsed = parse("function description", style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.style == Style.google

def test_parse_unsupported_style():
    """Test that an error is raised when using an unsupported style."""
    with pytest.raises(ValueError):
        parse("function description", style="unsupported_style")

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
___________ ERROR collecting test_docstring_parser_parser_parse_0.py ___________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_parser_parse_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_parser_parse_0.py:3: in <module>
    from docstring_parser.parser import DocstringParser, Style, STYLES, ParseError
E   ImportError: cannot import name 'DocstringParser' from 'docstring_parser.parser' (/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/parser.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_parser_parse_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""