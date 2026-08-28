
import pytest
from ansible.modules.apt_repository import _strip_username_password

def test_strip_username_password_with_at():
    result = _strip_username_password("user@example.com")
    assert result == "example.com"

def test_strip_username_password_without_at():
    result = _strip_username_password("pass@word123@example.com")
    assert result == "pass@word123@example.com"

def test_strip_username_password_no_at():
    result = _strip_username_password("example.com")
    assert result == "example.com"

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
_ ERROR collecting test_lib_ansible_modules_apt_repository__strip_username_password_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository__strip_username_password_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository__strip_username_password_0.py:3: in <module>
    from ansible.modules.apt_repository import _strip_username_password
E   ImportError: cannot import name '_strip_username_password' from 'ansible.modules.apt_repository' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/modules/apt_repository.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository__strip_username_password_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.41s ===============================
"""