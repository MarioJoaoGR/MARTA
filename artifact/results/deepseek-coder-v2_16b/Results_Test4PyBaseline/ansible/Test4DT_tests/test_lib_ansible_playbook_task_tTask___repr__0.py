
# Module: ansible.playbook.task
# test_task.py
from ansible.playbook.task import Task

def test_create_task_with_default_values():
    task = Task()
    assert hasattr(task, '_role'), "Task should have a role attribute"
    assert task._parent is None, "Default parent should be None"
    assert not hasattr(task, 'implicit'), "Implicit attribute should not be present by default"
    assert not hasattr(task, 'resolved_action'), "Resolved action should not be present by default"

def test_create_task_with_specific_role():
    task = Task(role='specificRole')
    assert task._role == 'specificRole', "Task role should be set to 'specificRole'"
    assert task._parent is None, "Default parent should still be None"
    assert not hasattr(task, 'implicit'), "Implicit attribute should not be present"
    assert not hasattr(task, 'resolved_action'), "Resolved action should not be present"

def test_create_task_including_another_task():
    included_task = Task()
    task = Task(task_include=included_task)
    assert task._parent is included_task, "Task parent should be the included task"
    assert not hasattr(task, 'implicit'), "Implicit attribute should not be present"
    assert not hasattr(task, 'resolved_action'), "Resolved action should not be present"

def test_create_task_with_block_and_role():
    block_data = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    task = Task(block=block_data, role='specificRole')
    assert task._role == 'specificRole', "Task role should be set to 'specificRole'"
    assert isinstance(task._parent, dict), "Parent should be a dictionary representing the block"
    assert task._parent['action'] == 'shell', "Block action should be 'shell'"
    assert task._parent['args']['cmd'] == 'echo hello', "Block argument cmd should be 'echo hello'"
    assert not hasattr(task, 'implicit'), "Implicit attribute should not be present"
    assert not hasattr(task, 'resolved_action'), "Resolved action should not be present"

def test_create_task_with_role_and_include():
    included_task = Task()
    task = Task(role='specificRole', task_include=included_task)
    assert task._role == 'specificRole', "Task role should be set to 'specificRole'"
    assert task._parent is included_task, "Task parent should be the included task"
    assert not hasattr(task, 'implicit'), "Implicit attribute should not be present"
    assert not hasattr(task, 'resolved_action'), "Resolved action should not be present"
