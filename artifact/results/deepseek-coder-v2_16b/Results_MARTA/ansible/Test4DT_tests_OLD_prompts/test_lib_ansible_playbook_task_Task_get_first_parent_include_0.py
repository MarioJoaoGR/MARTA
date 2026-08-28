
import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.task import Task
from ansible.playbook.task_include import TaskInclude

# Test case for get_first_parent_include with an invalid parent type

# Test case for get_first_parent_include with a valid TaskInclude parent
def test_get_first_parent_include_with_valid_parent():
    # Create a mock TaskInclude object
    mock_task_include = MagicMock(spec=TaskInclude)
    
    # Create a Task with the mock TaskInclude as its parent
    task = Task(task_include=mock_task_include)
    
    # Test that get_first_parent_include returns the mock TaskInclude object
    assert task.get_first_parent_include() is mock_task_include

# Test case for get_first_parent_include with no parent set
def test_get_first_parent_include_no_parent():
    # Create a Task without setting the parent
    task = Task()
    
    # Test that get_first_parent_include returns None when there is no parent set
    assert task.get_first_parent_include() is None