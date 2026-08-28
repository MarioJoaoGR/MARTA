
import pytest
from unittest.mock import patch
import socket
from tornado.netutil import bind_sockets

def test_bind_sockets_all_interfaces():
    with patch('socket.getaddrinfo', return_value=[
        (socket.AF_INET, socket.SOCK_STREAM, 0, '', ('127.0.0.1', 8080))
    ]):
        sockets = bind_sockets(8080)
        assert len(sockets) == 1
        assert sockets[0].getsockname()[1] == 8080

def test_bind_sockets_specific_ip():
    with patch('socket.getaddrinfo', return_value=[
        (socket.AF_INET, socket.SOCK_STREAM, 0, '', ('127.0.0.1', 8080))
    ]):
        sockets = bind_sockets(8080, "127.0.0.1")
        assert len(sockets) == 1
        assert sockets[0].getsockname()[0] == '127.0.0.1'

def test_bind_sockets_specific_ip_version():
    with patch('socket.getaddrinfo', return_value=[
        (socket.AF_INET6, socket.SOCK_STREAM, 0, '', ('::1', 8080))
    ]):
        sockets = bind_sockets(8080, "::1", family=socket.AF_INET6)
        assert len(sockets) == 1
        assert sockets[0].getsockname()[0] == '::1'

def test_bind_sockets_custom_backlog():
    with patch('socket.getaddrinfo', return_value=[
        (socket.AF_INET, socket.SOCK_STREAM, 0, '', ('127.0.0.1', 8080))
    ]):
        sockets = bind_sockets(8080, "127.0.0.1", backlog=1024)
        assert len(sockets) == 1
        sock = sockets[0]
        sock.listen(1024)

def test_bind_sockets_with_flags():
    with patch('socket.getaddrinfo', return_value=[
        (socket.AF_INET, socket.SOCK_STREAM, 0, '', ('127.0.0.1', 8080))
    ]):
        sockets = bind_sockets(8080, "127.0.0.1", flags=socket.AI_PASSIVE)
        assert len(sockets) == 1
        sock = sockets[0]
        sock.listen(128)  # Default backlog is used if not specified

def test_bind_sockets_reuse_port():
    with patch('socket.getaddrinfo', return_value=[
        (socket.AF_INET, socket.SOCK_STREAM, 0, '', ('127.0.0.1', 8080))
    ]):
        sockets = bind_sockets(8080, "127.0.0.1", reuse_port=True)
        assert len(sockets) == 1
        sock = sockets[0]
        assert sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT) == 1
