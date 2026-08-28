
import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleAssertionError, AnsibleParserError, AnsibleError


def test_edge_case():
    with pytest.raises(AnsibleParserError):
        play = Play.load({
            'hosts': [],
            'only_tags': [],
            'skip_tags': ['tag1'],
            'roles': []
        })

def test_invalid_input():
    with pytest.raises(AnsibleAssertionError):
        Play.load(None)