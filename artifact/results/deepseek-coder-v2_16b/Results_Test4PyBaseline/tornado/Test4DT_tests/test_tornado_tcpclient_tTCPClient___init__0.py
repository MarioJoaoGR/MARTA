
import pytest
from tornado.netutil import Resolver
from tornado.tcpclient import TCPClient

# Test creating a TCPClient instance with a custom resolver
def test_tcpclient_with_custom_resolver():
    from tornado.netutil import Resolver
    from tornado.tcpclient import TCPClient
    
    # Create a custom resolver or use an existing one
    resolver = Resolver()  # Replace this with your actual resolver implementation if needed
    tcp_client = TCPClient(resolver=resolver)
    
    assert isinstance(tcp_client.resolver, Resolver), "The resolver should be of type Resolver"
    assert not tcp_client._own_resolver, "The client should use the provided resolver and not create its own"

# Test creating a TCPClient instance without providing a resolver (defaulting to its own Resolver instance)
def test_tcpclient_without_resolver():
    from tornado.tcpclient import TCPClient
    
    tcp_client = TCPClient()
    
    assert isinstance(tcp_client.resolver, Resolver), "The default resolver should be of type Resolver"