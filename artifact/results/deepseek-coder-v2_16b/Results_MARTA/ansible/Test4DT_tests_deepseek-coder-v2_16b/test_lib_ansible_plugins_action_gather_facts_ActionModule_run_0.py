
import pytest
from ansible.plugins.action import ActionModule as AnsibleActionModule

@pytest.fixture(scope="module")
def action_module():
    return AnsibleActionModule()

# Test Scenario 1: Valid inputs - happy path
def test_valid_inputs_happy_path(action_module):
    task_vars = {
        'ansible_facts_parallel': True,
        'FACTS_MODULES': ['ansible.legacy.setup', 'custom.fact_module']
    }
    result = action_module.run(task_vars=task_vars)
    assert '_ansible_facts_gathered' in result['ansible_facts']
    assert not result.get('failed', False)
    assert not result.get('skipped', False)

# Test Scenario 2: Edge cases - None inputs or empty lists
def test_edge_cases(action_module):
    task_vars = {
        'FACTS_MODULES': None,
        'CONNECTION_FACTS_MODULES': {},
        'network_os': None
    }
    result = action_module.run(task_vars=task_vars)
    assert not '_ansible_facts_gathered' in result['ansible_facts']
    assert result.get('failed', False)
    assert result.get('skipped', False)

# Test Scenario 3: Invalid inputs - error handling
def test_invalid_inputs_error_handling(action_module):
    task_vars = {
        'ansible_facts_parallel': 'invalid_type',
        'FACTS_MODULES': ['invalid.module']
    }
    with pytest.raises(TypeError):
        action_module.run(task_vars=task_vars)
