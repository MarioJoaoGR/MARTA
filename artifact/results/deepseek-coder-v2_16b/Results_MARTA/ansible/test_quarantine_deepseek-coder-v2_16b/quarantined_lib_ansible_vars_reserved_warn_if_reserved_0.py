
import pytest
from your_module_name import warn_if_reserved

# Define a set of reserved names for testing purposes
_RESERVED_NAMES = {'var1', 'var2', 'vars'}

def test_warn_if_reserved_basic():
    with pytest.raises(SystemExit) as e:
        warn_if_reserved(['var1', 'var2', 'vars'])
    assert str(e.value) == "Found variable using reserved name: vars"

def test_warn_if_reserved_custom_reserved():
    custom_reserved = {'myvar'}
    with pytest.raises(SystemExit) as e:
        warn_if_reserved(['var1', 'var2'], custom_reserved)
    assert str(e.value) == "Found variable using reserved name: myvar"

def test_warn_if_reserved_no_additional():
    with pytest.raises(SystemExit) as e:
        warn_if_reserved(['var1', 'var2'])
    assert str(e.value) == "Found variable using reserved name: vars"

def test_warn_if_reserved_empty_list():
    with pytest.raises(SystemExit) as e:
        warn_if_reserved([])
    assert not hasattr(e.value, 'args')  # No warnings should be issued for an empty list

def test_warn_if_reserved_using_set():
    with pytest.raises(SystemExit) as e:
        warn_if_reserved({'var1', 'var2', 'vars'})
    assert str(e.value) == "Found variable using reserved name: vars"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
____ ERROR collecting test_lib_ansible_vars_reserved_warn_if_reserved_0.py _____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py:3: in <module>
    from your_module_name import warn_if_reserved
E   ModuleNotFoundError: No module named 'your_module_name'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_warn_if_reserved_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.39s ===============================
"""