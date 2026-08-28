
import pytest
from unittest.mock import patch
from ansible.executor.play_iterator import _failed_state_to_string

def test_no_failures():
    result = _failed_state_to_string(0)
    assert result == "FAILED_NONE"

def test_single_failure():
    result = _failed_state_to_string(1)
    assert result == "FAILED_SETUP"

def test_multiple_failures():
    result = _failed_state_to_string(3)  # 1 | 2
    assert result == "FAILED_SETUP|FAILED_TASKS"

def test_all_failures():
    result = _failed_state_to_string(15)  # 1 | 2 | 4 | 8
    assert result == "FAILED_SETUP|FAILED_TASKS|FAILED_RESCUE|FAILED_ALWAYS"

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
_ ERROR collecting test_lib_ansible_executor_play_iterator__failed_state_to_string_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_play_iterator__failed_state_to_string_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_play_iterator__failed_state_to_string_0.py:4: in <module>
    from ansible.executor.play_iterator import _failed_state_to_string
E   ImportError: cannot import name '_failed_state_to_string' from 'ansible.executor.play_iterator' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/play_iterator.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_play_iterator__failed_state_to_string_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.52s ===============================
"""