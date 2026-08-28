
import pytest
from ansible.playbook.task import Task
from ansible.errors import AnsibleParserError


def test_init_with_role():
    task = Task(role='example_role')
    assert task._role == 'example_role', "Task role should be set to 'example_role'"

