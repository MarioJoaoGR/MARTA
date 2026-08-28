
import pytest
from unittest.mock import patch, MagicMock
from tornado.tcpclient import _Connector
from tornado.ioloop import IOLoop
from tornado.concurrent import Future
import socket

def test_connector_initialization():
    addrinfo = [(socket.AF_INET, ('127.0.0.1', 80)), (socket.AF_INET6, ('::1', 80))]
    connect_mock = MagicMock()
    connector = _Connector(addrinfo, connect_mock)
    
    assert connector.io_loop == IOLoop.current()
    assert connector.connect == connect_mock
    assert isinstance(connector.future, Future)
    assert connector.timeout is None
    assert connector.connect_timeout is None
    assert connector.last_error is None
    assert connector.remaining == len(addrinfo)
    assert len(connector.primary_addrs) > 0 and len(connector.secondary_addrs) > 0
    assert isinstance(connector.streams, set)

