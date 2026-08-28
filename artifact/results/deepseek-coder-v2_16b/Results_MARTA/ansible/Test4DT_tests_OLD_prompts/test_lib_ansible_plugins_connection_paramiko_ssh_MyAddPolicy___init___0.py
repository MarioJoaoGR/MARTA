
import pytest
from unittest.mock import patch, MagicMock
from lib.ansible.plugins.connection.paramiko_ssh import MyAddPolicy

def test_edge_case():
    with pytest.raises(AttributeError):
        MyAddPolicy(None, None)

def test_invalid_input():
    with pytest.raises(AttributeError):
        MyAddPolicy("not a stdin", "not a connection")
