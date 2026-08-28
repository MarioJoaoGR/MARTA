
import pytest
from ansible.playbook.task import Task

def test_edge_cases():
    task = Task()
    with pytest.raises(KeyError):
        task._get_parent_attribute('some_attr')
