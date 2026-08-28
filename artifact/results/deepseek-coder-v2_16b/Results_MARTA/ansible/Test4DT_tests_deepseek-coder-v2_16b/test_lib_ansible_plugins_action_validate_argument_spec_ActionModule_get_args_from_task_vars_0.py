
import pytest
from ansible.plugins.action import ActionModule

# Test scenarios
def test_valid_inputs():
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    task_vars = {'name': 'John Doe', 'age': 30}
    action_module = ActionModule()
    args = action_module.get_args_from_task_vars(argument_spec, task_vars)
    
    assert isinstance(args['name'], str), "Name should be a string"
    assert isinstance(args['age'], int), "Age should be an integer"
    assert args == {'name': 'John Doe', 'age': 30}

def test_edge_cases():
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    task_vars = None
    action_module = ActionModule()
    args = action_module.get_args_from_task_vars(argument_spec, task_vars)
    
    assert args == {}, "Expected empty dictionary when task_vars is None"

def test_invalid_inputs():
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    task_vars = {'name': 123, 'age': 'thirty'}
    action_module = ActionModule()
    
    with pytest.raises(TypeError):
        args = action_module.get_args_from_task_vars(argument_spec, task_vars)
