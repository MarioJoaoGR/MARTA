
import pytest
from ansible.plugins.callback import TaskData, HostData
import time

# Test adding a host to a task when it doesn't exist yet
def test_add_host_new():
    task = TaskData(uuid='1234-5678', name='ExampleTask', path='/path/to/task', play=True, action='start')
    host = HostData(uuid='uuid123', name='host1', status='included', result='initial result')
    task.add_host(host)
    assert len(task.host_data) == 1
    assert task.host_data['uuid123'] == host

# Test adding a duplicate host to a task, which should raise an Exception
def test_add_duplicate_host():
    task = TaskData(uuid='1234-5678', name='ExampleTask', path='/path/to/task', play=True, action='start')
    host1 = HostData(uuid='uuid123', name='host1', status='included', result='result from host1')
    task.add_host(host1)  # Adding the first host
    
    with pytest.raises(Exception):
        host2 = HostData(uuid='uuid123', name='host2', status='included', result='result from host2')
        task.add_host(host2)  # Attempting to add a duplicate host will raise an Exception

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
_ ERROR collecting test_lib_ansible_plugins_callback_junit_TaskData_add_host_1.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_junit_TaskData_add_host_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_junit_TaskData_add_host_1.py:3: in <module>
    from ansible.plugins.callback import TaskData, HostData
E   ImportError: cannot import name 'TaskData' from 'ansible.plugins.callback' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/callback/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_junit_TaskData_add_host_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.98s ===============================
"""