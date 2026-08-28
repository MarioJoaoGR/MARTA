# Module: ansible.plugins.action.gather_facts
import pytest
from ansible.plugins.action import ActionModule as Am
import os
import time

# Assuming C is a configuration object that can be mocked or provided in tests
class ConfigMock:
    def __init__(self):
        self.config = {}
    
    def get_config_value(self, key, variables=None):
        return self.config.get(key, []) if variables is None else variables.get(key, [])

C = ConfigMock()

@pytest.fixture
def action_module():
    return Am()

# Test cases for serial execution mode
def test_run_serial_execution(action_module):
    task_vars = {
        'FACTS_MODULES': ['ansible.legacy.setup', 'custom.module'],
        'ansible_facts_parallel': False  # Explicitly set to serial execution
    }
    result = action_module.run(tmp=None, task_vars=task_vars)
    assert isinstance(result, dict), "Result should be a dictionary"
    assert 'ansible_facts' in result, "Result should contain ansible_facts"
    assert not result['failed'], "No modules should fail"
    assert len(result.get('skipped_modules', [])) == 0, "No modules should be skipped"

# Test cases for parallel execution mode
def test_run_parallel_execution(action_module):
    task_vars = {
        'FACTS_MODULES': ['ansible.legacy.setup', 'custom.module'],
        'ansible_facts_parallel': True  # Explicitly set to parallel execution
    }
    result = action_module.run(tmp=None, task_vars=task_vars)
    assert isinstance(result, dict), "Result should be a dictionary"
    assert 'ansible_facts' in result, "Result should contain ansible_facts"
    assert not result['failed'], "No modules should fail"
    assert len(result.get('skipped_modules', [])) == 0, "No modules should be skipped"

# Test cases for default execution mode (serial if not specified otherwise)
def test_run_default_execution(action_module):
    task_vars = {
        'FACTS_MODULES': ['ansible.legacy.setup', 'custom.module']
    }
    result = action_module.run(tmp=None, task_vars=task_vars)
    assert isinstance(result, dict), "Result should be a dictionary"
    assert 'ansible_facts' in result, "Result should contain ansible_facts"
    assert not result['failed'], "No modules should fail"
    assert len(result.get('skipped_modules', [])) == 0, "No modules should be skipped"

# Test cases for including smart module based on network OS
def test_run_smart_module_based_on_network_os(action_module):
    task_vars = {
        'FACTS_MODULES': ['ansible.legacy.setup', 'custom.module'],
        'network_os': 'ios'  # Example network operating system
    }
    result = action_module.run(tmp=None, task_vars=task_vars)
    assert isinstance(result, dict), "Result should be a dictionary"
    assert 'ansible_facts' in result, "Result should contain ansible_facts"
    assert not result['failed'], "No modules should fail"
    assert len(result.get('skipped_modules', [])) == 0, "No modules should be skipped"

# Test cases for handling task variables and temporary data
def test_run_handling_task_vars_and_temp_data(action_module):
    task_vars = {
        'FACTS_MODULES': ['ansible.legacy.setup', 'custom.module'],
        'network_os': 'ios'  # Example network operating system
    }
    tmp = {'temp_dir': '/path/to/temp'}  # Example temporary data
    result = action_module.run(tmp=tmp, task_vars=task_vars)
    assert isinstance(result, dict), "Result should be a dictionary"
    assert 'ansible_facts' in result, "Result should contain ansible_facts"
    assert not result['failed'], "No modules should fail"
    assert len(result.get('skipped_modules', [])) == 0, "No modules should be skipped"
