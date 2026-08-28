
import pytest
from thonny.roughparse import index2line

def test_index2line_valid_float():
    assert index2line(3.5) == 3

def test_index2line_valid_int():
    assert index2line(4) == 4

def test_index2line_valid_negative():
    assert index2line(-1) == -1

def test_index2line_invalid_string():
    assert index2line('abc') == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
___________ ERROR collecting test_thonny_roughparse_index2line_0.py ____________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_index2line_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_index2line_0.py:3: in <module>
    from thonny.roughparse import index2line
E   ImportError: cannot import name 'index2line' from 'thonny.roughparse' (/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/roughparse.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_index2line_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""