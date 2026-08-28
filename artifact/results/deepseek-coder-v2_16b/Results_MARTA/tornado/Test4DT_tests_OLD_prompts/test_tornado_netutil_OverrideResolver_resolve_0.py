
import pytest
from unittest.mock import patch, MagicMock
from tornado.netutil import OverrideResolver
import socket

def test_resolve_with_direct_mapping():
    with patch('tornado.netutil.Resolver', autospec=True) as mock_resolver:
        resolver = mock_resolver.return_value
        mapping = {
            "example.com": "127.0.0.1",
        }
        override_resolver = OverrideResolver(resolver=resolver, mapping=mapping)
        
        resolved_ips = override_resolver.resolve("example.com", 80)
        assert resolved_ips == resolver.resolve.return_value
        resolver.resolve.assert_called_once_with("127.0.0.1", 80, socket.AF_UNSPEC)

def test_resolve_with_host_port_mapping():
    with patch('tornado.netutil.Resolver', autospec=True) as mock_resolver:
        resolver = mock_resolver.return_value
        mapping = {
            ("login.example.com", 443): ("localhost", 1443),
        }
        override_resolver = OverrideResolver(resolver=resolver, mapping=mapping)
        
        resolved_ips = override_resolver.resolve("login.example.com", 443)
        assert resolved_ips == resolver.resolve.return_value
        resolver.resolve.assert_called_once_with("localhost", 1443, socket.AF_UNSPEC)

def test_resolve_with_host_port_family_mapping():
    with patch('tornado.netutil.Resolver', autospec=True) as mock_resolver:
        resolver = mock_resolver.return_value
        mapping = {
            ("login.example.com", 443, socket.AF_INET6): ("::1", 1443),
        }
        override_resolver = OverrideResolver(resolver=resolver, mapping=mapping)
        
        resolved_ips = override_resolver.resolve("login.example.com", 443, socket.AF_INET6)
        assert resolved_ips == resolver.resolve.return_value
        resolver.resolve.assert_called_once_with("::1", 1443, socket.AF_INET6)
