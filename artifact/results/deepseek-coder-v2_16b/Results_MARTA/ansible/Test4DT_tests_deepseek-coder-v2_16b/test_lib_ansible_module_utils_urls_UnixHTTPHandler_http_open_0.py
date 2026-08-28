
import pytest
from ansible.module_utils.urls import UnixHTTPHandler, UnixHTTPConnection

def test_unixhttphandler_init():
    handler = UnixHTTPHandler(unix_socket='/path/to/unix/socket')
    assert hasattr(handler, '_unix_socket'), "Unix socket attribute not set"
    assert handler._unix_socket == '/path/to/unix/socket', f"Expected unix_socket to be '/path/to/unix/socket' but got {handler._unix_socket}"

def test_unixhttpconnection_init():
    conn = UnixHTTPConnection(unix_socket='/path/to/unix/socket')
    assert hasattr(conn, '_unix_socket'), "Unix socket attribute not set"
    assert conn._unix_socket == '/path/to/unix/socket', f"Expected unix_socket to be '/path/to/unix/socket' but got {conn._unix_socket}"
