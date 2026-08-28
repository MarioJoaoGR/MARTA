
import pytest
from argparse import ArgumentParser
from httpie_help_formatter import HTTPieHelpFormatter

def test_httpie_help_formatter_basic():
    formatter = HTTPieHelpFormatter(max_help_position=7)
    parser = ArgumentParser(description="A command-line tool", formatter_class=HTTPieHelpFormatter)
    parser.add_argument("-H", "--header", dest="headers", action="append", help="Add a header")
    
    # Check if the argument is added correctly
    assert "-H, --header Add a header" in str(parser._actions[0].help)

def test_httpie_help_formatter_custom_max_help_position():
    formatter = HTTPieHelpFormatter(max_help_position=8)
    parser = ArgumentParser(description="A command-line tool", formatter_class=HTTPieHelpFormatter)
    parser.add_argument("-H", "--header", dest="headers", action="append", help="Add a header")
    
    # Check if the argument is added correctly with custom max_help_position
    assert "-H, --header Add a header" in str(parser._actions[0].help)

def test_httpie_help_formatter_split_lines():
    formatter = HTTPieHelpFormatter()
    text = "This is a test string with multiple lines.\nIt should be split correctly."
    
    # Split the text into lines
    lines = formatter._split_lines(text, 80)
    
    # Check if the text is split correctly
    assert len(lines) == 2
    assert lines[0] == "This is a test string with multiple lines."
    assert lines[1] == "It should be split correctly."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_httpie_cli_argparser_HTTPieHelpFormatter__split_lines_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieHelpFormatter__split_lines_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieHelpFormatter__split_lines_0.py:4: in <module>
    from httpie_help_formatter import HTTPieHelpFormatter
E   ModuleNotFoundError: No module named 'httpie_help_formatter'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieHelpFormatter__split_lines_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""