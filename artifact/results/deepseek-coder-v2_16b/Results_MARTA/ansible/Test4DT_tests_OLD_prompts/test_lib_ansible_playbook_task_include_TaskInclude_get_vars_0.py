
import pytest
from ansible.playbook.task_include import TaskInclude
from unittest.mock import patch, MagicMock



def test_get_vars_no_parent():
    task_include = TaskInclude(block={'file': 'path/to/task', '_raw_params': {'action': 'some_action', 'args': {'arg1': 'value1'}}})
    
    with pytest.raises(AttributeError):
        vars_dict = task_include.get_vars()