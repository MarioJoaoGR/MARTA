
import pytest
from unittest.mock import patch, MagicMock
import socket
from tornado.netutil import add_accept_handler

def test_add_accept_handler():
    # Create a mock socket and callback function
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 8888))
    sock.listen(128)
    
    def callback(conn: socket.socket, addr: tuple):
        pass
    
    # Call the function under test
    remove_handler = add_accept_handler(sock, callback)
    
    assert callable(remove_handler), "Expected a callable to be returned"
