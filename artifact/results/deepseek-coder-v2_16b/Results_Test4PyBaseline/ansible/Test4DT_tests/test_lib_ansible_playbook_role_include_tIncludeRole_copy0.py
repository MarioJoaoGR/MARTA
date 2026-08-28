# Module: ansible.playbook.role_include
import pytest
from ansible.playbook.role_include import IncludeRole

# Test initialization with default settings
def test_init_default():
    include_role = IncludeRole(role='my_role')
    assert include_role._parent_role == 'my_role'
    assert include_role._role_name is None
    assert include_role._role_path is None
    assert not hasattr(include_role, '_from_files')

# Test initialization with specific tasks
def test_init_with_tasks():
    include_role = IncludeRole(task_include=[{'name': 'task1'}, {'name': 'task2'}])
    assert not hasattr(include_role, '_parent_role')
    assert include_role._role_name is None
    assert not hasattr(include_role, '_role_path')
    assert include_role._from_files == {}

# Test initialization with all configuration options
def test_init_with_block():
    include_role = IncludeRole(block={'tasks': [{'name': 'task1'}, {'name': 'task2'}], 'vars': {'var1': 'value1'}, 'defaults': {'default1': 'value1'}})
    assert not hasattr(include_role, '_parent_role')
    assert include_role._role_name is None
    assert not hasattr(include_role, '_role_path')
    assert include_role._from_files == {}

# Test copy method with default settings
def test_copy_default():
    original = IncludeRole(role='my_role')
    copied = original.copy()
    assert copied._parent_role == 'my_role'
    assert copied._role_name is None
    assert copied._role_path is None
    assert not hasattr(copied, '_from_files')

# Test copy method with excluded parent and tasks
def test_copy_exclude():
    original = IncludeRole(block={'tasks': [{'name': 'task1'}, {'name': 'task2'}], 'vars': {'var1': 'value1'}, 'defaults': {'default1': 'value1'}})
    copied = original.copy(exclude_parent=True, exclude_tasks=True)
    assert not hasattr(copied, '_parent_role')
    assert not hasattr(copied, '_from_files')
    assert include_role._role_name is None
    assert include_role._role_path is None

if __name__ == "__main__":
    pytest.main()
