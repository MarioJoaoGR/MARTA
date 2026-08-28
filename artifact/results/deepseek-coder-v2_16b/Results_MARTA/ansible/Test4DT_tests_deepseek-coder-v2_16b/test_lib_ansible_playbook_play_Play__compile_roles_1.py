
import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleError, AnsibleParserError


def test_edge_case_none_values():
    datastructure = {
        'hosts': None,
        'gather_facts': None,
        'roles': None
    }
    with pytest.raises(AnsibleParserError):
        Play.load(datastructure)
