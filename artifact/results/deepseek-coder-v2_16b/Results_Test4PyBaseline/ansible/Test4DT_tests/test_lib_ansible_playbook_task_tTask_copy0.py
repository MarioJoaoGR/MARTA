# Module: ansible.playbook.task
# test_task.py
from ansible.playbook.task import Task

def test_default_initialization():
    task = Task()
    assert hasattr(task, '_args')
    assert hasattr(task, '_action')
    assert hasattr(task, '_async_val')
    assert hasattr(task, '_changed_when')
    assert hasattr(task, '_delay')
    assert hasattr(task, '_delegate_to')
    assert hasattr(task, '_delegate_facts')
    assert hasattr(task, '_failed_when')
    assert hasattr(task, '_loop')
    assert hasattr(task, '_loop_control')
    assert hasattr(task, '_notify')
    assert hasattr(task, '_poll')
    assert hasattr(task, '_register')
    assert hasattr(task, '_retries')
    assert hasattr(task, '_until')
    assert not hasattr(task, '_parent')
    assert not hasattr(task, '_role')
    assert task.implicit is False
    assert task.resolved_action is None

def test_specific_role_and_block():
    block_data = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    task = Task(block=block_data, role='exampleRole')
    assert hasattr(task, '_args')
    assert hasattr(task, '_action')
    assert hasattr(task, '_async_val')
    assert hasattr(task, '_changed_when')
    assert hasattr(task, '_delay')
    assert hasattr(task, '_delegate_to')
    assert hasattr(task, '_delegate_facts')
    assert hasattr(task, '_failed_when')
    assert hasattr(task, '_loop')
    assert hasattr(task, '_loop_control')
    assert hasattr(task, '_notify')
    assert hasattr(task, '_poll')
    assert hasattr(task, '_register')
    assert hasattr(task, '_retries')
    assert hasattr(task, '_until')
    assert not hasattr(task, '_parent')
    assert task._role == 'exampleRole'
    assert task.resolved_action == {'cmd': 'echo hello'}

def test_include_another_task():
    included_task = Task()
    task = Task(task_include=included_task)
    assert hasattr(task, '_args')
    assert hasattr(task, '_action')
    assert hasattr(task, '_async_val')
    assert hasattr(task, '_changed_when')
    assert hasattr(task, '_delay')
    assert hasattr(task, '_delegate_to')
    assert hasattr(task, '_delegate_facts')
    assert hasattr(task, '_failed_when')
    assert hasattr(task, '_loop')
    assert hasattr(task, '_loop_control')
    assert hasattr(task, '_notify')
    assert hasattr(task, '_poll')
    assert hasattr(task, '_register')
    assert hasattr(task, '_retries')
    assert hasattr(task, '_until')
    assert task._parent is not None
    assert isinstance(task._parent, Task)

def test_copying_task():
    included_task = Task()
    task = Task(task_include=included_task)
    new_task = task.copy(exclude_parent=True, exclude_tasks=True)
    assert not hasattr(new_task, '_parent')
    assert not hasattr(new_task, '_role')
    assert new_task.implicit is False
    assert new_task.resolved_action is None
