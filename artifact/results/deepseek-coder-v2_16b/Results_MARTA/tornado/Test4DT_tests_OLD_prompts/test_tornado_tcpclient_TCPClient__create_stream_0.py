
import pytest
from unittest.mock import patch, MagicMock
from tornado.tcpclient import TCPClient, Resolver, IOStream, Future
import socket

# Test valid inputs
def test_valid_inputs():
    with patch('tornado.tcpclient.Resolver', autospec=True):
        client = TCPClient(resolver=Resolver())
        assert isinstance(client.resolver, Resolver)
        assert client._own_resolver is False

# Test edge cases
def test_edge_cases():
    with patch('tornado.tcpclient.Resolver', autospec=True):
        client = TCPClient()
        assert isinstance(client.resolver, Resolver)
        assert client._own_resolver is True

# Test invalid inputs
def test_invalid_inputs():
    try:
        with patch('tornado.tcpclient.Resolver', autospec=True):
            client = TCPClient(resolver=None)
    except Exception as e:
        assert str(e) == "TypeError: __init__() missing 1 required positional argument: 'resolver'"
