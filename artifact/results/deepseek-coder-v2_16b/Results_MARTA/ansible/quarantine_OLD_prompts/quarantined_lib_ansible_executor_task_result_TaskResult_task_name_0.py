
import pytest
from unittest.mock import patch, MagicMock
from lib.ansible.executor.task_result import TaskResult
from lib.ansible.utils.data_loader import DataLoader

# Test 1: Creating an instance with dictionary return data
def test_create_instance_with_dict_return_data():
    host = 'localhost'
    task = 'update_packages'
    return_data = {'results': [{'skipped': True}, {'skipped': False}]}
    result = TaskResult(host, task, return_data)
    
    assert result._host == host
    assert result._task == task
    assert result._result == return_data

# Test 2: Creating an instance with string return data (mock DataLoader)
def test_create_instance_with_string_return_data():
    host = 'localhost'
    task = 'update_packages'
    return_data = {'results': [{'skipped': True}, {'skipped': False}]}
    
    with patch.object(DataLoader, 'load', return_value=return_data):
        result = TaskResult(host, task, return_data)
        
        assert result._host == host
        assert result._task == task
        assert result._result == return_data

# Test 3: Creating an instance with task fields
def test_create_instance_with_task_fields():
    host = 'localhost'
    task = MagicMock()
    task.get_name.return_value = "Custom Task"
    return_data = {'results': [{'skipped': True}, {'skipped': False}]}
    task_fields = {"name": "Example Task"}
    
    result = TaskResult(host, task, return_data, task_fields)
    
    assert result.task_name() == "Example Task"

# Test 4: Using TaskResult with a custom task object
def test_use_with_custom_task_object():
    host = 'localhost'
    task = MagicMock()
    task.get_name.return_value = "Custom Task"
    return_data = {'results': [{'skipped': True}, {'skipped': False}]}
    task_fields = {"name": "Example Task"}
    
    result = TaskResult(host, task, return_data, task_fields)
    
    assert result.task_name() == "Custom Task"

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
_ ERROR collecting test_lib_ansible_executor_task_result_TaskResult_task_name_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_task_result_TaskResult_task_name_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_task_result_TaskResult_task_name_0.py:5: in <module>
    from lib.ansible.utils.data_loader import DataLoader
E   ModuleNotFoundError: No module named 'lib.ansible.utils.data_loader'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_task_result_TaskResult_task_name_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.42s ===============================
"""