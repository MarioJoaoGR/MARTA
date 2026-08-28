
import pytest
from ansible.module_utils.connection import Connection
import socket


def test_valid_connection():
    valid_sock_path = '/tmp/valid_socket'
    conn = Connection(valid_sock_path)
    assert conn.socket_path == valid_sock_path
