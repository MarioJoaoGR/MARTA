
import pytest
from ColoramaPrinter import ColoramaPrinter
import colorama
from io import TextIOBase

def test_coloramaprinter_init():
    printer = ColoramaPrinter()
    assert isinstance(printer.ERROR, str)
    assert printer.ERROR == colorama.Fore.RED + "ERROR" + colorama.Style.RESET_ALL
    assert isinstance(printer.SUCCESS, str)
    assert printer.SUCCESS == colorama.Fore.GREEN + "SUCCESS" + colorama.Style.RESET_ALL
    assert isinstance(printer.ADDED_LINE, colorama.Fore)
    assert printer.ADDED_LINE == colorama.Fore.GREEN
    assert isinstance(printer.REMOVED_LINE, colorama.Fore)
    assert printer.REMOVED_LINE == colorama.Fore.RED

def test_coloramaprinter_init_with_output():
    class CustomOutput(TextIOBase):
        def write(self, text: str) -> None:
            self._written = text
    
    custom_output = CustomOutput()
    printer = ColoramaPrinter(output=custom_output)
    assert isinstance(printer.ERROR, str)
    assert printer.ERROR == colorama.Fore.RED + "ERROR" + colorama.Style.RESET_ALL
    assert isinstance(printer.SUCCESS, str)
    assert printer.SUCCESS == colorama.Fore.GREEN + "SUCCESS" + colorama.Style.RESET_ALL
    assert isinstance(printer.ADDED_LINE, colorama.Fore)
    assert printer.ADDED_LINE == colorama.Fore.GREEN
    assert isinstance(printer.REMOVED_LINE, colorama.Fore)
    assert printer.REMOVED_LINE == colorama.Fore.RED
    assert custom_output._written == colorama.Fore.RED + "ERROR" + colorama.Style.RESET_ALL

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
_______ ERROR collecting test_isort_format_ColoramaPrinter___init___0.py _______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_format_ColoramaPrinter___init___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_format_ColoramaPrinter___init___0.py:3: in <module>
    from ColoramaPrinter import ColoramaPrinter
E   ModuleNotFoundError: No module named 'ColoramaPrinter'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_format_ColoramaPrinter___init___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""