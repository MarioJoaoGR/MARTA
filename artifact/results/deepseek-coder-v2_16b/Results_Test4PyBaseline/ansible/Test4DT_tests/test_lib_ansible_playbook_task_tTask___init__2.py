
# Module: ansible.playbook.task
# test_task.py
from ansible.playbook.task import Task
import pytest

def test_default_init():
    # Test creating a new Task instance with default values
    task = Task()
    assert task is not None, "Task creation failed"
    assert task._parent is None, "Default parent should be None"