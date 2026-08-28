
import pytest
from unittest.mock import patch, MagicMock
import socket
from tornado.netutil import _resolve_addr


def test_valid_hostname():
    with patch('tornado.netutil._resolve_addr', autospec=True) as mock_resolve_addr:
        mock_resolve_addr.return_value = [("AF_INET", "127.0.0.1")]
        results = _resolve_addr("localhost", 80)
        assert len(results) > 0, "Expected at least one result for valid hostname"

def test_valid_ip():
    with patch('tornado.netutil._resolve_addr', autospec=True) as mock_resolve_addr:
        mock_resolve_addr.return_value = [("AF_INET", "192.168.1.100")]
        results = _resolve_addr("192.168.1.100", 80)
        assert len(results) > 0, "Expected at least one result for valid IP address"