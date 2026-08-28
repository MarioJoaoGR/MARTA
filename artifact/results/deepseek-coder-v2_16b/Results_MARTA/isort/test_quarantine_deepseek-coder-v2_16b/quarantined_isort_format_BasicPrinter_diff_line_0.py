
import pytest
from basic_printer import BasicPrinter, print_message
from io import StringIO
import sys

# Test for the BasicPrinter class initialization with default output (stdout)
def test_basic_printer_default_output():
    printer = BasicPrinter()
    captured_output = StringIO()
    sys.stdout = captured_output
    print_message("Test message", "SUCCESS")
    assert captured_output.getvalue().strip() == "Test message"
    sys.stdout = sys.__stdout__

# Test for the BasicPrinter class initialization with custom output (file)
def test_basic_printer_custom_output():
    file = StringIO()
    printer = BasicPrinter(file)
    print_message("Custom message", "SUCCESS", printer=printer)
    assert file.getvalue().strip() == "Custom message"

# Test for the diff_line method of BasicPrinter class
def test_basic_printer_diff_line():
    printer = BasicPrinter(StringIO())
    line = "This is a test line."
    captured_output = StringIO()
    sys.stdout = captured_output
    printer.diff_line(line)
    assert captured_output.getvalue().strip() == line
    sys.stdout = sys.__stdout__

# Test for the print_message function with SUCCESS status
def test_print_message_success():
    captured_output = StringIO()
    sys.stdout = captured_output
    print_message("Test success message", "SUCCESS")
    assert captured_output.getvalue().strip() == "Test success message"
    sys.stdout = sys.__stdout__

# Test for the print_message function with ERROR status
def test_print_message_error():
    captured_output = StringIO()
    sys.stdout = captured_output
    print_message("Test error message", "ERROR")
    assert captured_output.getvalue().strip() == "Test error message"
    sys.stdout = sys.__stdout__

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
/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_format_BasicPrinter_diff_line_0.py:3: in <module>
    from basic_printer import BasicPrinter, print_message
E   ModuleNotFoundError: No module named 'basic_printer'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_format_BasicPrinter_diff_line_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""