
import pytest
from ansible.playbook.task import Task
from ansible.errors import AnsibleParserError
from ansible.playbook.loop_control import LoopControl

def test_valid_input():
    loop_control_dict = {
        "items": ["item1", "item2"],
        "labels": ["label1", "label2"]
    }
    task = Task(block={}, role=None, task_include=None)
    task._loop_control = LoopControl()
    
    with pytest.raises(AnsibleParserError):
        task._load_loop_control("loop_control", loop_control_dict)
