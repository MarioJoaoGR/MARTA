
import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.task import Task
from unittest.mock import patch, MagicMock


def test_edge_cases():
    with pytest.raises(AnsibleParserError):
        task = Task()
        task._load_loop_control('test', 'invalid data')