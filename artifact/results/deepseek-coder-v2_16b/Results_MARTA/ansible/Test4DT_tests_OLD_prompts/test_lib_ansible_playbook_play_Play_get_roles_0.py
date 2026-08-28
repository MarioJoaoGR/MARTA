
import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.play import Play
from ansible.errors import AnsibleError

# Test for valid input scenario

# Test for edge case scenario where hosts list is empty
def test_edge_case():
    data = {
        'hosts': [],
        'gather_facts': False,
        'roles': ['backup']
    }
    with pytest.raises(AnsibleError):
        Play.load(data)

# Test for invalid input scenario where required fields are missing