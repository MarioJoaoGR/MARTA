
import pytest
from ansible.module_utils.urls import UnixHTTPConnection

def test_valid_init():
    unix_socket = '/path/to/unix/socket'
    connection = UnixHTTPConnection(unix_socket)
    assert connection._unix_socket == unix_socket
