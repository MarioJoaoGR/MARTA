
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.scripts.ansible_connection_cli_stub import ConnectionProcess, JsonRpcServer


def test_invalid_inputs():
    mock_play_context = {'hosts': 'localhost'}
    mock_socket_path = '/tmp/socket'
    mock_original_path = '/path/to/original'
    mock_fd = 123

    with patch('ansible.cli.scripts.ansible_connection_cli_stub.JsonRpcServer') as MockJsonRpcServer:
        conn_process = ConnectionProcess(fd=mock_fd, play_context=mock_play_context, socket_path=mock_socket_path, original_path=mock_original_path)

        with pytest.raises(Exception):
            raise Exception("Expected exception was not raised")