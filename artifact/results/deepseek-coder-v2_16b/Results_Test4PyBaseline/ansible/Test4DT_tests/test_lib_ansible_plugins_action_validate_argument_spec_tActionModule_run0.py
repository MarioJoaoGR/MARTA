# Module: ansible.plugins.action.validate_argument_spec
import pytest
from ansible.plugins.action import ActionModule
from ansible.errors import AnsibleError

# Assuming the necessary imports for the test are already done

def test_get_args_from_task_vars():
    action_instance = ActionModule()
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'}
    }
    task_vars = {
        'name': 'John',
        'age': 30
    }
    
    validated_args = action_instance.get_args_from_task_vars(argument_spec, task_vars)
    assert isinstance(validated_args, dict), "Expected a dictionary but got something else"
    assert len(validated_args) == 2, "Expected two arguments to be validated"
    assert 'name' in validated_args and isinstance(validated_args['name'], str), "Name should be a string"
    assert 'age' in validated_args and isinstance(validated_args['age'], int), "Age should be an integer"

def test_run_with_missing_argument_spec():
    action_instance = ActionModule()
    task_vars = {
        'provided_arguments': {
            'name': 'John',
            'age': 30
        }
    }
    
    with pytest.raises(AnsibleError) as excinfo:
        action_instance.run(task_vars=task_vars)
    assert '"argument_spec" arg is required in args' in str(excinfo.value), "Expected an error about missing argument_spec"

def test_run_with_incorrect_types():
    action_instance = ActionModule()
    task_vars = {
        'argument_spec': [1, 2],  # Incorrect type for argument_spec
        'provided_arguments': {
            'name': 'John',
            'age': 30
        }
    }
    
    with pytest.raises(AnsibleError) as excinfo:
        action_instance.run(task_vars=task_vars)
    assert 'Incorrect type for argument_spec, expected dict and got <class' in str(excinfo.value), "Expected an error about incorrect type for argument_spec"

def test_run_with_incorrect_provided_arguments():
    action_instance = ActionModule()
    task_vars = {
        'argument_spec': {
            'name': {'type': 'str'},
            'age': {'type': 'int'}
        },
        'provided_arguments': [1, 2]  # Incorrect type for provided_arguments
    }
    
    with pytest.raises(AnsibleError) as excinfo:
        action_instance.run(task_vars=task_vars)
    assert 'Incorrect type for provided_arguments, expected dict and got <class' in str(excinfo.value), "Expected an error about incorrect type for provided_arguments"

def test_run_with_validation_errors():
    action_instance = ActionModule()
    task_vars = {
        'argument_spec': {
            'name': {'type': 'str'},
            'age': {'type': 'int'}
        },
        'provided_arguments': {
            'name': 123,  # name should be a string but is an int
            'age': 30
        }
    }
    
    result = action_instance.run(task_vars=task_vars)
    assert result['failed'], "Expected validation to fail"
    assert 'Validation of arguments failed:' in result['msg'], "Expected a meaningful error message"
    assert len(result['argument_errors']) == 1, "Expected one validation error"
    assert isinstance(result['argument_errors'][0], str), "Each error should be a string"

def test_run_with_no_validation_errors():
    action_instance = ActionModule()
    task_vars = {
        'argument_spec': {
            'name': {'type': 'str'},
            'age': {'type': 'int'}
        },
        'provided_arguments': {
            'name': 'John',
            'age': 30
        }
    }
    
    result = action_instance.run(task_vars=task_vars)
    assert not result['failed'], "Expected validation to pass"
    assert 'Validation of arguments failed:' not in result['msg'], "No errors should be reported if validation passes"
