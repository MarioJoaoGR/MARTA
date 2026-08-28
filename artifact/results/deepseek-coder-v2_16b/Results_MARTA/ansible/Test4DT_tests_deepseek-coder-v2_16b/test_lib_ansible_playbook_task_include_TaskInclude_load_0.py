
import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.errors import AnsibleParserError


def test_load_with_invalid_data():
    data = {
        '_raw_params': {'action': 'some_action', 'args': {'arg1': 'value1'}, 'invalid_key': 'invalid_value'}
    }
    with pytest.raises(AnsibleParserError):
        TaskInclude.load(data)