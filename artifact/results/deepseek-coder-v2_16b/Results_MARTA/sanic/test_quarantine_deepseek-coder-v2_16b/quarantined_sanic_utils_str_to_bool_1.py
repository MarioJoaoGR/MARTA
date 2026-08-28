
import pytest
from your_module import str_to_bool  # Replace 'your_module' with the actual module name where str_to_bool is defined

def test_str_to_bool_true():
    assert str_to_bool("Y") == True
    assert str_to_bool("Yes") == True
    assert str_to_bool("1") == True
    assert str_to_bool("True") == True
    assert str_to_bool("ON") == True
    assert str_to_bool("ENABLE") == True

def test_str_to_bool_false():
    assert str_to_bool("N") == False
    assert str_to_bool("No") == False
    assert str_to_bool("0") == False
    assert str_to_bool("False") == False
    assert str_to_bool("OFF") == False
    assert str_to_bool("DISABLE") == False

def test_str_to_bool_invalid():
    with pytest.raises(ValueError):
        str_to_bool("maybe")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
______________ ERROR collecting test_sanic_utils_str_to_bool_1.py ______________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_utils_str_to_bool_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_utils_str_to_bool_1.py:3: in <module>
    from your_module import str_to_bool  # Replace 'your_module' with the actual module name where str_to_bool is defined
E   ModuleNotFoundError: No module named 'your_module'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_utils_str_to_bool_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""