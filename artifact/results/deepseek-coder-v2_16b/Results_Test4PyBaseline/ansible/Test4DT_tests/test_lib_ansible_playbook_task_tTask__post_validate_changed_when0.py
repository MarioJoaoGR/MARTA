
# Module: ansible.playbook.task
# test_task.py
from ansible.playbook.task import Task

def test_default_task():
    # Test creating a new task instance with default values
    task = Task()
    assert hasattr(task, '_role'), "Task should have an attribute _role"
    assert getattr(task, '_role') is None, "_role should be None by default"
    assert task._parent is None, "_parent should be None by default"