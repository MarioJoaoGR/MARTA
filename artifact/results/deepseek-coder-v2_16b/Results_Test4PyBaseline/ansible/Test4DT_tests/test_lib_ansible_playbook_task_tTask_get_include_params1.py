
# Module: ansible.playbook.task
# test_task.py
from ansible.playbook.task import Task

def test_get_include_params_no_parent():
    task = Task()
    assert task.get_include_params() == {}, "Task with no parent should return an empty dictionary"

def test_get_include_params_with_parent():
    parent_task = Task()
    parent_task._parent = None  # Simulate a hypothetical scenario where the parent is not set correctly
    task = Task()
    task._parent = parent_task
    assert task.get_include_params() == {}, "Task with no include params should return an empty dictionary"

def test_get_include_params_with_action():
    task = Task()
    task.vars = {"key": "value"}  # Simulate having vars in the action