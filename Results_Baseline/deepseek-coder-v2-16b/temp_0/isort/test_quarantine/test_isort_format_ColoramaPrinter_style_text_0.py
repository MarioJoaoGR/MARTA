
import pytest
from io import StringIO
import sys
from colorama import Fore, Style  # pylint: disable=E0401
from isort.format import ColoramaPrinter

def test_coloramaprinter_init():
    output = StringIO()
    printer = ColoramaPrinter(error="ERROR", success="SUCCESS", output=output)
    
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_isort_format_ColoramaPrinter_style_text_0.py _
ImportError while importing test module '/projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_format_ColoramaPrinter_style_text_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/local/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
isort/Test4DT_tests/test_isort_format_ColoramaPrinter_style_text_0.py:5: in <module>
    from colorama import Fore, Style  # pylint: disable=E0401
E   ModuleNotFoundError: No module named 'colorama'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR isort/Test4DT_tests/test_isort_format_ColoramaPrinter_style_text_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""