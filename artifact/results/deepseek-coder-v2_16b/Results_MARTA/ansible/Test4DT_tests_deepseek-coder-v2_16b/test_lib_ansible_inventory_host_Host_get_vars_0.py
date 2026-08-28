
import pytest
from ansible.inventory.host import Host

def test_edge_case():
    with pytest.raises(ValueError):
        host = Host(name=None, port='invalid')
