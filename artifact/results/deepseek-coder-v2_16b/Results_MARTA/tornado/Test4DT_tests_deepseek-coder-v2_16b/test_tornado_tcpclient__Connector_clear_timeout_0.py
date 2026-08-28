
import pytest
from tornado import ioloop, netutil
from tornado.concurrent import Future
import socket

# Assuming _Connector is defined as per the provided code snippet
class _Connector:
    def __init__(self, addrinfo, connect):
        self.io_loop = ioloop.IOLoop.current()
        self.connect = connect
        self.future = Future()
        self.timeout = None
        self.connect_timeout = None
        self.last_error = None
        self.remaining = len(addrinfo)
        self.primary_addrs, self.secondary_addrs = self.split(addrinfo)
        self.streams = set()

    def split(self, addrinfo):
        primary = []
        secondary = []
        for af, addr in addrinfo:
            if af == socket.AF_INET:
                primary.append((af, addr))
            else:
                secondary.append((af, addr))
        return primary, secondary

    def clear_timeout(self):
        if self.timeout is not None:
            self.io_loop.remove_timeout(self.timeout)

# Mock connect function for testing
def my_connect(af, addr):
    sock = netutil.new_socket(af, socket.SOCK_STREAM)
    stream = IOStream(sock)
    future = Future()
    sock.connect(addr, lambda: future.set_result((stream, future)))
    return (stream, future)

# Test scenarios
def test_valid_inputs():
    addrinfo = [(socket.AF_INET, ('127.0.0.1', 80)), (socket.AF_INET6, ('::1', 80))]
    connector = _Connector(addrinfo, my_connect)
    assert len(connector.primary_addrs) == 1
    assert len(connector.secondary_addrs) == 1
    assert isinstance(connector.primary_addrs[0][1], tuple)
    assert isinstance(connector.secondary_addrs[0][1], tuple)

def test_edge_cases():
    addrinfo = []
    connector = _Connector(addrinfo, my_connect)
    assert len(connector.primary_addrs) == 0
    assert len(connector.secondary_addrs) == 0

def test_invalid_inputs():
    with pytest.raises(TypeError):
        _Connector(None, None)
