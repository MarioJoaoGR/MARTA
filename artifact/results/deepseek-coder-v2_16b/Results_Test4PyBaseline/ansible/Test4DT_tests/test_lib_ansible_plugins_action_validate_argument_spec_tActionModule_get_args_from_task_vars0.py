# Module: ansible.plugins.action.validate_argument_spec
import pytest
from ansible.plugins.action.validate_argument_spec import ActionModule

# Assuming self is an instance of ActionModule for the purpose of these tests
@pytest.fixture
def action_module():
    return ActionModule()

@pytest.mark.parametrize("argument_spec, task_vars, expected", [
    (
        {'name': {'type': 'str'}, 'age': {'type': 'int'}},
        {'name': 'John', 'age': 30},
        {'name': 'John', 'age': 30}
    ),
    (
        {'full_name': {'type': 'str'}, 'birthyear': {'type': 'int'}},
        {'full_name': '{{ username }}', 'birthyear': 1990},
        {'full_name': 'John', 'birthyear': 1990}  # Assuming username is not provided, so full_name remains templated
    ),
    (
        {'username': {'type': 'str'}, 'age': {'type': 'int'}},
        {'username': 'JohnDoe'},
        {'username': 'JohnDoe', 'age': 30}  # Assuming age is derived from some other source or default value
    ),
    (
        {'name': {'type': 'str'}, 'age': {'type': 'int'}},
        {},
        {}
    ),
    (
        {'first_name': {'type': 'str'}, 'last_name': {'type': 'str'}, 'age': {'type': 'int'}},
        {'first_name': 'John', 'last_name': 'Doe'},
        {'first_name': 'John', 'last_name': 'Doe', 'age': 30}  # Assuming age is derived from some other source or default value
    )
])
def test_get_args_from_task_vars(action_module, argument_spec, task_vars, expected):
    args = action_module.get_args_from_task_vars(argument_spec, task_vars)
    assert args == expected
