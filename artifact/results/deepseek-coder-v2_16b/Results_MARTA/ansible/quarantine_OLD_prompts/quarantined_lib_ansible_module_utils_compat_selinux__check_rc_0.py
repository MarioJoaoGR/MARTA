
import pytest
from unittest.mock import patch
from ansible.module_utils.compat.selinux import get_errno, _check_rc
import os

def test_check_rc_with_negative_value():
    with patch('ansible.module_utils.compat.selinux.get_errno', return_value=1):
        with pytest.raises(OSError) as excinfo:
            _check_rc(-1)
        assert excinfo.value.errno == 1
        assert str(excinfo.value) == os.strerror(1)

def test_check_rc_with_non_negative_value():
    result = _check_rc(0)
    assert result == 0

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
_ ERROR collecting test_lib_ansible_module_utils_compat_selinux__check_rc_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_compat_selinux__check_rc_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_compat_selinux__check_rc_0.py:4: in <module>
    from ansible.module_utils.compat.selinux import get_errno, _check_rc
E   ImportError: cannot import name '_check_rc' from 'ansible.module_utils.compat.selinux' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/compat/selinux.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_compat_selinux__check_rc_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.35s ===============================
"""