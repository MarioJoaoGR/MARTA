
import sys
from unittest.mock import patch
from io import StringIO
from basic_printer import BasicPrinter, print_message

def test_print_success_message():
    # Create a buffer to capture output
    captured_output = StringIO()
    with patch('sys.stdout', new=captured_output):
        print_message("The operation was successful!", "SUCCESS")
    assert captured_output.getvalue().strip() == "The operation was successful!"

def test_print_error_message():
    # Create a buffer to capture output
    captured_output = StringIO()
    with patch('sys.stdout', new=captured_output):
        print_message("An error occurred: Unable to connect to database.", "ERROR")
    assert captured_output.getvalue().strip() == "An error occurred: Unable to connect to database."

def test_print_default_output():
    # Create a buffer to capture output
    captured_output = StringIO()
    with patch('sys.stdout', new=captured_output):
        print_message("This is a standard message.", "SUCCESS")
    assert captured_output.getvalue().strip() == "This is a standard message."

def test_print_custom_status():
    # Create a buffer to capture output
    captured_output = StringIO()
    with patch('sys.stdout', new=captured_output):
        print_message("This is an informational message.", "INFO")
    assert captured_output.getvalue().strip() == "This is an informational message."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
________ ERROR collecting test_isort_format_BasicPrinter_diff_line_0.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_format_BasicPrinter_diff_line_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_format_BasicPrinter_diff_line_0.py:5: in <module>
    from basic_printer import BasicPrinter, print_message
E   ModuleNotFoundError: No module named 'basic_printer'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_format_BasicPrinter_diff_line_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""