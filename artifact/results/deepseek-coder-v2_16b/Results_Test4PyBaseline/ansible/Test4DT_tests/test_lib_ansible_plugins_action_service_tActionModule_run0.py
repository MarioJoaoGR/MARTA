# Module: ansible.plugins.action.service
import pytest
from ansible.plugins.action import ActionModule

# Fixture to create an instance of the ActionModule for testing
@pytest.fixture
def action_module():
    return ActionModule()

# Test cases for the run method of ActionModule
def test_run_automatically_detecting_service_manager(action_module):
    result = action_module.run(task_vars={})
    assert 'module' in result, f"Expected 'module' key to be in result but got {result}"
    assert result['module'] == 'ansible.legacy.service', f"Expected module to be 'ansible.legacy.service' but got {result['module']}"

def test_run_explicitly_specifying_systemd(action_module):
    result = action_module.run(task_vars={'use': 'systemd'})
    assert 'module' in result, f"Expected 'module' key to be in result but got {result}"
    assert result['module'] == 'ansible.legacy.service', f"Expected module to be 'ansible.legacy.service' but got {result['module']}"

def test_run_using_check_mode(action_module):
    result = action_module.run(task_vars={'use': 'auto', 'check_mode': True})
    assert 'module' in result, f"Expected 'module' key to be in result but got {result}"
    assert result['module'] == 'ansible.legacy.service', f"Expected module to be 'ansible.legacy.service' but got {result['module']}"

def test_run_delegating_to_another_host(action_module):
    result = action_module.run(task_vars={'use': 'auto', 'delegate_to': 'otherhost'})
    assert 'module' in result, f"Expected 'module' key to be in result but got {result}"
    assert result['module'] == 'ansible.legacy.service', f"Expected module to be 'ansible.legacy.service' but got {result['module']}"

def test_run_specifying_unused_parameters_for_systemd(action_module):
    result = action_module.run(task_vars={'use': 'systemd', 'pattern': 'all', 'runlevel': 3, 'sleep': 10})
    assert 'module' in result, f"Expected 'module' key to be in result but got {result}"
    assert result['module'] == 'ansible.legacy.service', f"Expected module to be 'ansible.legacy.service' but got {result['module']}"
    assert 'warnings' in result, f"Expected warnings to be in result but got {result}"
    assert "Ignoring 'pattern'" in result['warnings'][0], f"Expected warning about ignoring 'pattern' not to be in result: {result['warnings']}"
    assert "Ignoring 'runlevel'" in result['warnings'][1], f"Expected warning about ignoring 'runlevel' not to be in result: {result['warnings']}"
    assert "Ignoring 'sleep'" in result['warnings'][2], f"Expected warning about ignoring 'sleep' not to be in result: {result['warnings']}"
