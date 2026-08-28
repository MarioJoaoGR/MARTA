
import pytest
from ansible.cli.scripts.ansible_connection_cli_stub import ConnectionProcess
import os

# Test 1: Valid initialization of ConnectionProcess
def test_valid_initialization():
    fd = 12345
    play_context = {'hosts': 'localhost'}
    socket_path = '/tmp/socket'
    original_path = '/path/to/original'
    
    conn_process = ConnectionProcess(fd=fd, play_context=play_context, socket_path=socket_path, original_path=original_path)
    
    assert conn_process.fd == fd
    assert conn_process.play_context == play_context
    assert conn_process.socket_path == socket_path
    assert conn_process.original_path == original_path

# Test 2: Shutdown method should remove the socket file and lock file if they exist