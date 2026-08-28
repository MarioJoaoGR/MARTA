
import pytest
from lib.ansible.plugins.callback import TaskData, HostData
import time

# Test initialization of TaskData class
def test_taskdata_initialization():
    task = TaskData(uuid='1234-5678', name='ExampleTask', path='/path/to/task', play=True, action='start')
    assert task.uuid == '1234-5678'
    assert task.name == 'ExampleTask'
    assert task.play is True
    assert task.action == 'start'
    assert isinstance(task.start, float)
    assert task.host_data == {}

# Test adding a host to TaskData class
def test_add_host():
    task = TaskData(uuid='1234-5678', name='ExampleTask', path='/path/to/task', play=True, action='start')
    host = HostData(uuid='uuid123', name='host1', status='included', result='initial result')
    task.add_host(host)
    assert len(task.host_data) == 1
    assert task.host_data['uuid123'] == host

# Test adding a duplicate host to TaskData class
def test_duplicate_host():
    task = TaskData(uuid='1234-5678', name='ExampleTask', path='/path/to/task', play=True, action='start')
    host1 = HostData(uuid='uuid123', name='host1', status='included', result='result from host1')
    task.add_host(host1)  # Adding the first host
    
    with pytest.raises(Exception) as e:
        host2 = HostData(uuid='uuid123', name='host2', status='included', result='result from host2')
        task.add_host(host2)  # Attempting to add a duplicate host will raise an Exception
    
    assert str(e.value) == '/path/to/task: True: ExampleTask: duplicate host callback: host2'

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
_ ERROR collecting test_lib_ansible_plugins_callback_junit_TaskData_add_host_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_junit_TaskData_add_host_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_junit_TaskData_add_host_0.py:3: in <module>
    from lib.ansible.plugins.callback import TaskData, HostData
E   ImportError: cannot import name 'TaskData' from 'lib.ansible.plugins.callback' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/callback/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_junit_TaskData_add_host_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.49s ===============================
"""