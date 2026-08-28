
import pytest
from ansible.playbook.role_include import IncludeRole

# Test Case 1: Including a Role with Default Settings
def test_include_role_default():
    include_role = IncludeRole(role='my_role')
    assert hasattr(include_role, '_parent_role'), "IncludeRole instance should have _parent_role attribute"
    assert include_role._parent_role == 'my_role', f"Expected role to be 'my_role' but got {include_role._parent_role}"

# Test Case 2: Including Specific Tasks from a Role
def test_include_role_with_tasks():
    tasks = [{'name': 'task1'}, {'name': 'task2'}]
    include_role = IncludeRole(task_include=tasks)
    assert hasattr(include_role, '_from_files'), "IncludeRole instance should have _from_files attribute"