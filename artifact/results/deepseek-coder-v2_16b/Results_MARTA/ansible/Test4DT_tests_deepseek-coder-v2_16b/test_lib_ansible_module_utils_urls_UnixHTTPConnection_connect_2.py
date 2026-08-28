
import pytest
from ansible.module_utils.urls import UnixHTTPConnection
import socket

def test_none_input():
    with pytest.raises(TypeError):
        UnixHTTPConnection()

def test_invalid_path():
    invalid_socket = "invalid/path"
    with pytest.raises(OSError):
        connection = UnixHTTPConnection(invalid_socket)
        connection.connect()
