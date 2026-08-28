
import pytest
from unittest.mock import patch
import sys
from io import StringIO
from basic_printer import BasicPrinter, print_message

def test_print_success_message():
    # Prepare a mock output that captures the printed message
    captured_output = StringIO()
    sys.stdout = captured_output
    
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        print_message("The operation was successful!", "SUCCESS")
        assert mock_stdout.getvalue().strip() == "The operation was successful!"
        
    # Restore the original stdout
    sys.stdout = sys.__stdout__

def test_print_error_message():
    # Prepare a mock output that captures the printed message
    captured_output = StringIO()
    sys.stdout = captured_output
    
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        print_message("An error occurred: Unable to connect to database.", "ERROR")
        assert mock_stdout.getvalue().strip() == "\033[91mAn error occurred: Unable to connect to database.\033[0m"
        
    # Restore the original stdout
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
________ ERROR collecting test_isort_format_BasicPrinter___init___0.py _________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_format_BasicPrinter___init___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_format_BasicPrinter___init___0.py:6: in <module>
    from basic_printer import BasicPrinter, print_message
E   ModuleNotFoundError: No module named 'basic_printer'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_format_BasicPrinter___init___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""