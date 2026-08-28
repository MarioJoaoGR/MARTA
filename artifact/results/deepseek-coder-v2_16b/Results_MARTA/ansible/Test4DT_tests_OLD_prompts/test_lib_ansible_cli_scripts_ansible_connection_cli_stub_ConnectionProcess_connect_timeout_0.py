
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.scripts.ansible_connection_cli_stub import ConnectionProcess

def test_invalid_inputs():
    with pytest.raises(TypeError):
        ConnectionProcess()
