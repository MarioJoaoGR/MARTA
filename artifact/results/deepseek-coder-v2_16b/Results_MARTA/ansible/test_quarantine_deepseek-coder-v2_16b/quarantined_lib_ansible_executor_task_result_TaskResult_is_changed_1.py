
import pytest
from ansible.executor.task_result import TaskResult
from ansible.utils.data_loader import DataLoader

# Test for checking if a task is changed
def test_is_changed():
    # Create a TaskResult instance with 'changed' key set to True
    task_result = TaskResult(host='localhost', task='update_packages', return_data={'results': [{'changed': True}, {'changed': False}]})
    assert task_result.is_changed() is True

    # Create a TaskResult instance with 'changed' key set to False
    task_result = TaskResult(host='localhost', task='update_packages', return_data={'results': [{'changed': False}, {'changed': False}]})
    assert task_result.is_changed() is False

# Test for checking if a task needs a debugger based on globally enabled flag
def test_needs_debugger():
    # Create a TaskResult instance with the need for a debugger
    task_result = TaskResult(host='localhost', task='update_packages', return_data={'results': [{'failed': True, 'needs_debugger': True}, {'failed': False, 'needs_debugger': False}]})
    assert task_result.needs_debugger(globally_enabled=True) is True

    # Create a TaskResult instance without the need for a debugger
    task_result = TaskResult(host='localhost', task='update_packages', return_data={'results': [{'failed': True, 'needs_debugger': False}, {'failed': False, 'needs_debugger': False}]})
    assert task_result.needs_debugger(globally_enabled=True) is False

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
_ ERROR collecting test_lib_ansible_executor_task_result_TaskResult_is_changed_1.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_task_result_TaskResult_is_changed_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_task_result_TaskResult_is_changed_1.py:4: in <module>
    from ansible.utils.data_loader import DataLoader
E   ModuleNotFoundError: No module named 'ansible.utils.data_loader'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_task_result_TaskResult_is_changed_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.82s ===============================
"""