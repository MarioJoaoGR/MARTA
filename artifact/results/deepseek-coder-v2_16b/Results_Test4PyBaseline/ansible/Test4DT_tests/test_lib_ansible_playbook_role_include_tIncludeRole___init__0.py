
import pytest
from ansible.playbook.role_include import IncludeRole

# Test Case 1: Including a Role by Name with Default Settings
def test_include_role_default():
    include_role = IncludeRole(role='my_role')
    assert hasattr(include_role, '_parent_role'), "Expected _parent_role attribute to be set"
    assert include_role._parent_role == 'my_role', f"Expected role name to be 'my_role' but got {include_role._parent_role}"

# Test Case 2: Including Specific Tasks from a Role
def test_include_role_with_tasks():
    tasks = [{'name': 'task1'}, {'name': 'task2'}]
    include_role = IncludeRole(task_include=tasks)
    assert hasattr(include_role, '_parent_role'), "Expected _parent_role attribute to be set"