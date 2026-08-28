
import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError


def test_edge_case_none_or_empty_list():
    invalid_config = {
        'hosts': None,
        'tasks': []
    }
    with pytest.raises(AnsibleParserError) as excinfo:
        Play.load(invalid_config)
    assert "Hosts list cannot be empty" in str(excinfo.value), "Expected error message about hosts being empty"