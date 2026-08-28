# Module: ansible.plugins.action.wait_for_connection
import pytest
from ansible.plugins.action import ActionModule
from datetime import datetime, timedelta
import time

# Assuming the module is imported correctly from its namespace
# from ansible.plugins.action.wait_for_connection import ActionModule as Am

@pytest.fixture
def action_module():
    return ActionModule()

def test_run_basic(action_module):
    task_vars = {'ansible_facts': {}}
    result = action_module.run(tmp=None, task_vars=task_vars)
    assert 'failed' not in result, "Expected no failure"
    assert 'skipped' not in result, "Expected not to be skipped"
    assert 'elapsed' in result, "Elapsed time should be recorded"

def test_run_with_custom_args(action_module):
    task_vars = {'ansible_facts': {}}
    custom_args = {
        'connect_timeout': 10,
        'delay': 5,
        'sleep': 2,
        'timeout': 900
    }
    result = action_module.run(tmp=None, task_vars=task_vars, **custom_args)
    assert 'failed' not in result, "Expected no failure"
    assert 'skipped' not in result, "Expected not to be skipped"
    assert 'elapsed' in result, "Elapsed time should be recorded"

def test_run_in_check_mode(action_module):
    task_vars = {'ansible_facts': {}}
    result = action_module.run(tmp=None, task_vars=task_vars, check_mode=True)
    assert 'failed' not in result, "Expected no failure"
    assert 'skipped' in result and result['skipped'], "Expected to be skipped due to check mode"

def test_run_with_custom_connect_timeout_delay_sleep_and_timeout(action_module):
    task_vars = {'ansible_facts': {}}
    custom_args = {
        'connect_timeout': 15,
        'delay': 3,
        'sleep': 1.5,
        'timeout': 1200
    }
    result = action_module.run(tmp=None, task_vars=task_vars, **custom_args)
    assert 'failed' not in result, "Expected no failure"
    assert 'skipped' not in result, "Expected not to be skipped"
    assert 'elapsed' in result, "Elapsed time should be recorded"

def test_run_with_timeout_failure(action_module):
    task_vars = {'ansible_facts': {}}
    # Simulate a situation where the ping module test fails due to timeout
    with pytest.raises(Exception) as e:
        action_module.run(tmp=None, task_vars=task_vars, connect_timeout=1, delay=0, sleep=0, timeout=1)
    assert 'failed' in str(e.value), "Expected a failure due to timeout"
