
import pytest
from ansible.plugins.action import set_stats

@pytest.fixture
def valid_instance():
    action_instance = set_stats.ActionModule()
    task_vars = {'data': {'key1': 'value1', 'key2': 2}, 'aggregate': True, 'per_host': False}
    action_instance._task_vars = task_vars
    return action_instance

@pytest.fixture
def edge_case_instance():
    action_instance = set_stats.ActionModule()
    task_vars = {'data': None, 'aggregate': False, 'per_host': True}
    action_instance._task_vars = task_vars
    return action_instance

@pytest.fixture
def invalid_instance():
    action_instance = set_stats.ActionModule()
    task_vars = {'data': [], 'aggregate': 123, 'per_host': 'true'}
    action_instance._task_vars = task_vars
    return action_instance

def test_valid_inputs(valid_instance):
    result = valid_instance.run()
    assert 'ansible_stats' in result
    assert isinstance(result['ansible_stats'], dict)
    assert 'data' in result['ansible_stats']
    assert isinstance(result['ansible_stats']['data'], dict)
    assert 'key1' in result['ansible_stats']['data']
    assert result['ansible_stats']['data']['key1'] == 'value1'
    assert 'key2' in result['ansible_stats']['data']
    assert result['ansible_stats']['data']['key2'] == 2
    assert 'aggregate' in result['ansible_stats']
    assert result['ansible_stats']['aggregate'] is True
    assert 'per_host' in result['ansible_stats']
    assert result['ansible_stats']['per_host'] is False

def test_edge_cases(edge_case_instance):
    result = edge_case_instance.run()
    assert 'ansible_stats' in result
    assert isinstance(result['ansible_stats'], dict)
    assert 'data' not in result['ansible_stats']
    assert 'aggregate' not in result['ansible_stats']
    assert 'per_host' not in result['ansible_stats']

def test_invalid_inputs(invalid_instance):
    with pytest.raises(TypeError) as excinfo:
        invalid_instance.run()
    assert "The 'data' option needs to be a dictionary/hash" in str(excinfo.value)
