
import pytest
from tornado.netutil import Resolver
from tornado.tcpclient import TCPClient

def test_default_init():
    tcp_client = TCPClient()
    assert isinstance(tcp_client.resolver, Resolver)
    assert tcp_client._own_resolver is True

def test_custom_resolver_init():
    resolver = Resolver()
    tcp_client = TCPClient(resolver=resolver)
    assert tcp_client.resolver == resolver