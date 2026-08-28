
import pytest
from ansible.playbook.task import Task

# Test Case 1: Creating a Task with Default Values
def test_create_task_with_default_values():
    task = Task()
    assert hasattr(task, '_role'), "Task should have an attribute _role"
    assert getattr(task, '_role') is None, "_role should be None by default"