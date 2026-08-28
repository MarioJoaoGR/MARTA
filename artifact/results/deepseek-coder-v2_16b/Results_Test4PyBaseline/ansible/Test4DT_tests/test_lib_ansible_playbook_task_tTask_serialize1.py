
import pytest
from ansible.playbook.task import Task

# Test creating a Task with default values including serialization method
def test_create_task_with_default_values():
    task = Task()
    assert hasattr(task, '_role'), "Task should have a role attribute"
    assert task._role is None, "Default role should be None"
    assert not hasattr(task, 'parent'), "Task should not have a parent by default"
    serialized_data = task.serialize()
    assert isinstance(serialized_data, dict), "Serialized data should be a dictionary"
    assert 'parent' not in serialized_data, "Default serialization should not include 'parent'"
    assert 'role' not in serialized_data, "Default serialization should not include 'role'"