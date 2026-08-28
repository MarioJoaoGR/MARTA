
import pytest
from unittest.mock import patch
from io import StringIO
from BasicPrinter import BasicPrinter, print_message

def test_print_success_message():
    # Create a buffer to capture the output
    captured_output = StringIO()
    
    # Create an instance of BasicPrinter with the captured output
    printer = BasicPrinter(captured_output)
    
    # Call the print_message function with success status and message
    print_message("The operation was successful!", "SUCCESS")
    
    # Assert that the printed message is correct
    assert captured_output.getvalue().strip() == 'SUCCESS: The operation was successful!'

def test_print_error_message():
    # Create a buffer to capture the output
    captured_output = StringIO()
    
    # Create an instance of BasicPrinter with the captured output
    printer = BasicPrinter(captured_output)
    
    # Call the print_message function with error status and message
    print_message("An error occurred: Unable to connect to database.", "ERROR")
    
    # Assert that the printed message is correct
    assert captured_output.getvalue().strip() == 'ERROR: An error occurred: Unable to connect to database.'

def test_print_success_message_default_output():
    # Create a buffer to capture the output
    captured_output = StringIO()
    
    # Patch sys.stdout to use the captured output
    with patch('sys.stdout', new=captured_output):
        # Call the print_message function with success status and message
        print_message("A simple message.", "SUCCESS")
        
    # Assert that the printed message is correct
    assert captured_output.getvalue().strip() == 'SUCCESS: A simple message.'

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
_________ ERROR collecting test_isort_format_BasicPrinter_success_0.py _________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_format_BasicPrinter_success_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_format_BasicPrinter_success_0.py:5: in <module>
    from BasicPrinter import BasicPrinter, print_message
E   ModuleNotFoundError: No module named 'BasicPrinter'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_format_BasicPrinter_success_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""