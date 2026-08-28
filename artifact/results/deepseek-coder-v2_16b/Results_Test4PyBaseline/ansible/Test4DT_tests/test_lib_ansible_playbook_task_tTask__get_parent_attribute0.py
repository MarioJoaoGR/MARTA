
import pytest
from ansible.playbook.task import Task

# Test cases for the Task class initialization and attribute handling
def test_task_initialization():
    # Test creating a task with only role
    task1 = Task(role='setup')
    assert hasattr(task1, '_role'), "Task should have an _role attribute"
    assert task1._role == 'setup', "Role should be set to 'setup'"
    
    # Test creating a task with block and role
    block_data = {'key': 'value'}
    task2 = Task(block=block_data, role='exampleRole')
    assert hasattr(task2, '_role'), "Task should have an _role attribute"
    assert task2._role == 'exampleRole', "Role should be set to 'exampleRole'"
    assert task2._parent is not None, "Task should have a parent when initialized with block and role"
    
    # Test creating a task including another task
    included_task = Task()
    task3 = Task(task_include=included_task)
    assert hasattr(task3, '_parent'), "Task should have a _parent attribute"
    assert task3._parent is not None, "Task should have a parent when initialized with task_include"

# Test cases for the _get_parent_attribute method
def test_get_parent_attribute():
    # Create a sample Task object and set up its parent
    parent = Task()
    task = Task(task_include=parent)
    
    # Ensure that _get_parent_attribute returns the correct value when extend is False