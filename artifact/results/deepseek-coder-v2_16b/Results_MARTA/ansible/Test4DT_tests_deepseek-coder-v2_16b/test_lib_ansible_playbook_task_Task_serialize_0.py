
import pytest
from ansible.playbook.task import Task


def test_create_task_with_role():
    task = Task(role='example_role')
    assert task._role == 'example_role', "Expected role to be 'example_role'"

def test_include_another_task():
    included_task = Task(block={'action': 'shell', 'args': {'cmd': 'echo hello'}})
    main_task = Task(task_include=included_task)
    assert main_task._parent is not None, "Expected task to include another task"
    assert isinstance(main_task._parent, Task), "Expected the parent of the included task to be a Task instance"