
import pytest
import socket
from typing import List, Optional

# Import the function from the module
from tornado.netutil import bind_sockets

def test_bind_sockets_default():
    """Test binding to all available interfaces on a specific port."""
    sockets = bind_sockets(port=8080)
    assert len(sockets) > 0, "Expected at least one socket bound to the port."
    for sock in sockets:
        assert sock.getsockname()[1] == 8080, f"Expected port 8080 but got {sock.getsockname()[1]}"

def test_bind_sockets_specific_address():
    """Test binding to a specific IP address."""
    sockets = bind_sockets(port=8080, address='127.0.0.1')
    assert len(sockets) > 0, "Expected at least one socket bound to the specified address."
    for sock in sockets:
        addr = sock.getsockname()
        assert addr[0] == '127.0.0.1', f"Expected IP address '127.0.0.1' but got {addr[0]}"
        assert addr[1] == 8080, f"Expected port 8080 but got {addr[1]}"

def test_bind_sockets_ipv6():
    """Test binding to a specific IPv6 address."""
    sockets = bind_sockets(port=8080, address='::1', family=socket.AF_INET6)
    assert len(sockets) > 0, "Expected at least one socket bound to the specified IPv6 address."
    for sock in sockets:
        addr = sock.getsockname()
        assert addr[0] == '::1', f"Expected IP address '::1' but got {addr[0]}"
        assert addr[1] == 8080, f"Expected port 8080 but got {addr[1]}"

def test_bind_sockets_reuse_port():
    """Test binding with reuse_port option enabled."""
    sockets = bind_sockets(port=8080, reuse_port=True)
    assert len(sockets) > 0, "Expected at least one socket bound to the port with reuse_port."
    for sock in sockets:
        try:
            assert sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT) == 1, "Expected SO_REUSEPORT to be enabled."
        except AttributeError:
            pytest.skip("Platform does not support SO_REUSEPORT.")

def test_bind_sockets_custom_backlog():
    """Test binding with a custom backlog size."""
    sockets = bind_sockets(port=8080, backlog=128)