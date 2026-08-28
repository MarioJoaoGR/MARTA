
# Module: ansible.playbook.task
# test_task.py
from ansible.playbook.task import Task

def test_create_task_with_default_values():
    task = Task()
    assert hasattr(task, '_role'), "Task should have a _role attribute"
    assert task._parent is None, "Default parent should be None"