
from io import StringIO
import pytest
from flutes.io import _ReverseReadlineFile, reverse_lines_generator

def test_error_handling():
    fp = StringIO("Hello, world!\n")
    gen = reverse_lines_generator()
    rev_readline = _ReverseReadlineFile(fp, gen)
    
    with pytest.raises(NotImplementedError):
        rev_readline.readline()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_flutes_io__ReverseReadlineFile___init___2_test_error_handling.py _
ImportError while importing test module '/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___init___2_test_error_handling.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/local/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___init___2_test_error_handling.py:4: in <module>
    from flutes.io import _ReverseReadlineFile, reverse_lines_generator
E   ImportError: cannot import name 'reverse_lines_generator' from 'flutes.io' (/projects/F202407648IACDCF2/mario/flutes/flutes/io.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___init___2_test_error_handling.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.17s ===============================
"""