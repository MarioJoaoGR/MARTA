
import pytest
from sty.primitive import Renderfuncs  # Correctly importing Renderfuncs
from sty.Register import Register  # Importing the Register class

def test_valid_case():
    register = Register()
    assert isinstance(register.as_namedtuple(), tuple), "Expected a namedtuple"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_sty_primitive_Register_as_namedtuple_0_test_valid_case.py _
ImportError while importing test module '/Users/mario/Desktop/GECAD/Test4Py/sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_0_test_valid_case.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_0_test_valid_case.py:4: in <module>
    from sty.Register import Register  # Importing the Register class
E   ModuleNotFoundError: No module named 'sty.Register'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_0_test_valid_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.06s ===============================
"""