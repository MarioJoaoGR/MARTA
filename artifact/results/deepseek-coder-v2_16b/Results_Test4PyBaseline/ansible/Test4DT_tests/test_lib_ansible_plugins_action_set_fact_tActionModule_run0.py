# Module: ansible.plugins.action.set_fact
import pytest
from ansible.plugins.action import ActionModule
from ansible.errors import AnsibleActionFail
from ansible.utils.boolean import boolean
from collections import Iterable
import string

# Assuming self is bound to an instance of ActionModule for the purpose of these tests
@pytest.fixture
def action_module():
    return ActionModule()

def test_run_basic_usage(action_module):
    task_vars = {'key1': 'value1', 'key2': 'value2'}
    result = action_module.run(tmp=None, task_vars=task_vars)
    assert isinstance(result['ansible_facts'], dict), "Expected ansible_facts to be a dictionary"
    assert len(result['ansible_facts']) == 2, "Expected two facts to be created"
    assert result['ansible_facts'] == {'key1': 'value1', 'key2': 'value2'}, "Facts do not match the provided task variables"
    assert isinstance(result['_ansible_facts_cacheable'], bool), "_ansible_facts_cacheable should be a boolean"
    assert result['_ansible_facts_cacheable'] is False, "_ansible_facts_cacheable should be False by default"

def test_run_with_cacheable_argument(action_module):
    task_vars = {'key1': 'value1', 'cacheable': True}
    result = action_module.run(tmp=None, task_vars=task_vars)
    assert isinstance(result['ansible_facts'], dict), "Expected ansible_facts to be a dictionary"
    assert len(result['ansible_facts']) == 1, "Expected one fact to be created"
    assert result['ansible_facts'] == {'key1': 'value1'}, "Facts do not match the provided task variables"
    assert isinstance(result['_ansible_facts_cacheable'], bool), "_ansible_facts_cacheable should be a boolean"
    assert result['_ansible_facts_cacheable'] is True, "_ansible_facts_cacheable should be set to True"

def test_run_no_key_value_pairs(action_module):
    task_vars = {}
    with pytest.raises(AnsibleActionFail) as excinfo:
        action_module.run(tmp=None, task_vars=task_vars)
    assert str(excinfo.value) == 'No key/value pairs provided, at least one is required for this action to succeed', "Expected a specific error message"

def test_run_invalid_variable_name(action_module):
    task_vars = {'invalid-key': 'value1'}
    with pytest.raises(AnsibleActionFail) as excinfo:
        action_module.run(tmp=None, task_vars=task_vars)
    assert str(excinfo.value) == "The variable name 'invalid-key' is not valid. Variables must start with a letter or underscore character, and contain only letters, numbers and underscores.", "Expected a specific error message"

def test_run_with_boolean_values(action_module):
    task_vars = {'bool_true': True, 'bool_false': False}
    result = action_module.run(tmp=None, task_vars=task_vars)
    assert isinstance(result['ansible_facts'], dict), "Expected ansible_facts to be a dictionary"
    assert len(result['ansible_facts']) == 2, "Expected two facts to be created"
    assert result['ansible_facts'] == {'bool_true': True, 'bool_false': False}, "Facts do not match the provided task variables"
    assert isinstance(result['_ansible_facts_cacheable'], bool), "_ansible_facts_cacheable should be a boolean"
    assert result['_ansible_facts_cacheable'] is False, "_ansible_facts_cacheable should be False by default"
