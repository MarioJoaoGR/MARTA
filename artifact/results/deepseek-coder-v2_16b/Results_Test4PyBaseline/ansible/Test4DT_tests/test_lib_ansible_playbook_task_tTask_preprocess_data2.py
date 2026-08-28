
import pytest
from ansible.playbook.task import Task
from ansible.errors import AnsibleAssertionError, AnsibleParserError

# Test creating a blank task instance
def test_create_blank_task():
    task = Task()
    assert hasattr(task, '_role'), "Task should have an attribute _role"
    assert task._parent is None, "Task parent should be None by default"