
import pytest
from ansible.playbook.helpers import load_list_of_tasks
from ansible.errors import AnsibleParserError, AnsibleAssertionError


def test_invalid_inputs():
    ds = [{'invalid': 'data'}]
    play = {}
    with pytest.raises(AnsibleParserError):
        load_list_of_tasks(ds, play)

