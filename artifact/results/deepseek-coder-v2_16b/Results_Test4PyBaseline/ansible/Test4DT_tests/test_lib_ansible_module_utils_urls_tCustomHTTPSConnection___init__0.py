# Module: ansible.module_utils.urls
import pytest
from unittest.mock import patch
from ansible.module_utils.urls import CustomHTTPSConnection

# Test cases for CustomHTTPSConnection class
def test_basic_usage():
    with patch('httplib.HTTPSConnection') as mock_conn:
        conn = CustomHTTPSConnection('example.com', 443)
        assert conn.cert_file is None
        assert conn.key_file is None
        assert conn.context is None
        mock_conn.assert_called_once_with('example.com', 443)

def test_with_additional_arguments():
    with patch('httplib.HTTPSConnection') as mock_conn:
        conn = CustomHTTPSConnection('example.com', 443, timeout=10)
        assert conn.cert_file is None
        assert conn.key_file is None
        assert conn.context is None
        mock_conn.assert_called_once_with('example.com', 443, timeout=10)

def test_using_source_address():
    with patch('httplib.HTTPSConnection') as mock_conn:
        conn = CustomHTTPSConnection('example.com', 443, source_address=('192.168.1.100', 8080))
        assert conn.cert_file is None
        assert conn.key_file is None
        assert conn.context is None
        mock_conn.assert_called_once_with('example.com', 443, source_address=('192.168.1.100', 8080))

def test_with_proxy_tunneling():
    with patch('httplib.HTTPSConnection') as mock_conn:
        conn = CustomHTTPSConnection('example.com', 443, _tunnel_host='proxy.example.com')
        assert conn.cert_file is None
        assert conn.key_file is None
        assert conn.context is None
        mock_conn.assert_called_once_with('example.com', 443, _tunnel_host='proxy.example.com')

def test_load_cert_chain():
    with patch('httplib.HTTPSConnection') as mock_conn:
        conn = CustomHTTPSConnection('example.com', 443)
        conn.cert_file = 'path/to/certificate.pem'
        conn.key_file = 'path/to/private_key.pem'
        with patch('ssl.SSLContext.load_cert_chain') as mock_load:
            conn.context.load_cert_chain(conn.cert_file, conn.key_file)
            mock_load.assert_called_once_with(conn.cert_file, conn.key_file)
