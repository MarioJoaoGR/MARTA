
import pytest
from unittest.mock import patch
from ansible.playbook.task import Task

# Assuming templar and env are defined somewhere in your module or imported modules
# Example definitions for testing purposes
class Templar:
    def template(self, value, convert_bare=False):
        return value  # Simplified implementation for testing

env = {}
templar = Templar()

def _parse_env_kv(k, v):
    try:
        env[k] = templar.template(v, convert_bare=False)
    except AnsibleUndefinedVariable as e:
        error = to_native(e)
        if self.action in C._ACTION_FACT_GATHERING and 'ansible_facts.env' in error or 'ansible_env' in error:
            # ignore as fact gathering is required for 'env' facts
            return
        raise

# Test cases
def test_valid_input():
    with patch('your_module._parse_env_kv') as mock_parse:
        task = Task()  # Assuming Task is defined in ansible.playbook.task
        task.args = {'key': 'MY_VAR', 'value': 'my_value'}
        _parse_env_kv(task.args['key'], task.args['value'])
        mock_parse.assert_called_once_with('MY_VAR', 'my_value')

def test_edge_case():
    with patch('your_module._parse_env_kv') as mock_parse:
        task = Task()  # Assuming Task is defined in ansible.playbook.task
        task.args = {'key': None, 'value': None}
        with pytest.raises(ValueError):
            _parse_env_kv(task.args['key'], task.args['value'])
        mock_parse.assert_called_once_with(None, None)

def test_invalid_input():
    with patch('your_module._parse_env_kv') as mock_parse:
        task = Task()  # Assuming Task is defined in ansible.playbook.task
        task.args = {'key': 123, 'value': 'my_value'}
        with pytest.raises(ValueError):
            _parse_env_kv(task.args['key'], task.args['value'])
        mock_parse.assert_called_once_with(123, 'my_value')
