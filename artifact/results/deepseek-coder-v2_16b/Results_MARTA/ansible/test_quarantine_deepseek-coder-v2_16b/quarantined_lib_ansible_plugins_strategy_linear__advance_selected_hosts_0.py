
import pytest
from ansible.plugins.strategy.linear import _advance_selected_hosts

# Test Case 1: Basic Usage
def test_basic_usage():
    class Host:
        def __init__(self, name):
            self.name = name
    
    class Task:
        def __init__(self, run_state, cur_block):
            self.run_state = run_state
            self.cur_block = cur_block
    
    hosts = [Host('host1'), Host('host2'), Host('host3')]
    host_tasks = {
        'host1': (Task('running', 1), None),
        'host2': (Task('pending', 1), None),
        'host3': (Task('completed', 1), None)
    }
    
    expected_output = [('host1', Task('running', 1)), ('host2', Task('pending', 1))]
    result = _advance_selected_hosts(hosts, 1, 'running')
    assert len(result) == len(expected_output)
    for i in range(len(result)):
        assert result[i][0].name == expected_output[i][0].name
        assert result[i][1].run_state == expected_output[i][1].run_state
        assert result[i][1].cur_block == expected_output[i][1].cur_block

# Test Case 2: Handling No Active Tasks or Incorrect State
def test_no_active_tasks():
    class Host:
        def __init__(self, name):
            self.name = name
    
    hosts = [Host('host1'), Host('host2')]
    host_tasks = {
        'host1': (Task('stopped', 1), None),
        'host2': (Task('completed', 1), None)
    }
    
    expected_output = []
    result = _advance_selected_hosts(hosts, 1, 'running')
    assert len(result) == len(expected_output)

# Test Case 3: Handling No Hosts Provided
def test_no_hosts():
    hosts = []
    host_tasks = {}
    
    expected_output = []
    result = _advance_selected_hosts(hosts, 1, 'running')
    assert len(result) == len(expected_output)

# Test Case 4: Handling Multiple Hosts and Tasks
def test_multiple_hosts():
    class Host:
        def __init__(self, name):
            self.name = name
    
    class Task:
        def __init__(self, run_state, cur_block):
            self.run_state = run_state
            self.cur_block = cur_block
    
    hosts = [Host('host1'), Host('host2'), Host('host3')]
    host_tasks = {
        'host1': (Task('running', 1), None),
        'host2': (Task('pending', 1), None),
        'host3': (Task('completed', 1), None)
    }
    
    expected_output = [('host1', Task('running', 1)), ('host2', Task('pending', 1))]
    result = _advance_selected_hosts(hosts, 1, 'running')
    assert len(result) == len(expected_output)
    for i in range(len(result)):
        assert result[i][0].name == expected_output[i][0].name
        assert result[i][1].run_state == expected_output[i][1].run_state
        assert result[i][1].cur_block == expected_output[i][1].cur_block

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
_ ERROR collecting test_lib_ansible_plugins_strategy_linear__advance_selected_hosts_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_strategy_linear__advance_selected_hosts_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_strategy_linear__advance_selected_hosts_0.py:3: in <module>
    from ansible.plugins.strategy.linear import _advance_selected_hosts
E   ImportError: cannot import name '_advance_selected_hosts' from 'ansible.plugins.strategy.linear' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/strategy/linear.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_strategy_linear__advance_selected_hosts_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.70s ===============================
"""