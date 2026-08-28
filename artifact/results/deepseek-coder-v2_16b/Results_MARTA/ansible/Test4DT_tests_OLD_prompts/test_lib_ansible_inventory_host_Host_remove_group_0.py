
import pytest
from unittest.mock import patch, MagicMock
from ansible.inventory.host import Host


def test_edge_case():
    host = Host(name='exampleHost')
    with pytest.raises(TypeError):
        host.remove_group()
