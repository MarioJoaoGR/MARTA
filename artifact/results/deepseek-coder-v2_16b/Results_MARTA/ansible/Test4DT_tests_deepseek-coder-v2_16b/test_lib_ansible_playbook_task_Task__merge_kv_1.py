
import pytest
from ansible.playbook.task import Task

def test_valid_inputs():
    task = Task()
    result = task._merge_kv({'key1': 'value1', 'key2': 'value2'})
    assert result == 'key1=value1 key2=value2'

