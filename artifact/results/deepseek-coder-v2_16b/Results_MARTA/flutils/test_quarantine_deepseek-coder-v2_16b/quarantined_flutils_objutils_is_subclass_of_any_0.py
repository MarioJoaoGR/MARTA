
import pytest
from flutils.objutils import is_subclass_of_any
from collections import ValuesView, KeysView, UserList

def test_is_subclass_of_any_true():
    obj = dict(a=1, b=2).keys()
    result = is_subclass_of_any(obj.__class__, ValuesView, KeysView, UserList)
    assert result == True

def test_is_subclass_of_any_false():
    obj = [1, 2, 3]
    result = is_subclass_of_any(obj.__class__, ValuesView, KeysView, UserList)
    assert result == False

def test_is_subclass_of_any_string():
    obj = "example"
    result = is_subclass_of_any(obj.__class__, ValuesView, KeysView, UserList)
    assert result == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
________ ERROR collecting test_flutils_objutils_is_subclass_of_any_0.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_objutils_is_subclass_of_any_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_objutils_is_subclass_of_any_0.py:4: in <module>
    from collections import ValuesView, KeysView, UserList
E   ImportError: cannot import name 'ValuesView' from 'collections' (/opt/conda/envs/test4py_env/lib/python3.10/collections/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_objutils_is_subclass_of_any_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""