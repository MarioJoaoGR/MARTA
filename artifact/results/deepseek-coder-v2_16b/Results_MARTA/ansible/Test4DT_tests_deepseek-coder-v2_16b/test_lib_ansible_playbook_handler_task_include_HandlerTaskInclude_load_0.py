
import pytest
from ansible.playbook.handler_task_include import HandlerTaskInclude
from ansible.errors import AnsibleAssertionError, AnsibleParserError

def test_valid_inputs():
    handler = HandlerTaskInclude()
    with pytest.raises(AnsibleParserError):
        result = handler.load(data={'key': 'value'}, block='some_block', role='some_role', task_include=['task1', 'task2'])

