# Module: ansible.module_utils.urls
import pytest
from unittest.mock import patch
import urllib_request
from ansible.module_utils.urls import HTTPSClientAuthHandler

# Test cases for HTTPSClientAuthHandler class
def test_httpsclientauthhandler_init():
    handler = HTTPSClientAuthHandler(client_cert="path/to/client_cert.pem", client_key="path/to/client_key.pem")
    assert handler.client_cert == "path/to/client_cert.pem"
    assert handler.client_key == "path/to/client_key.pem"
    assert not hasattr(handler, "_unix_socket")  # _unix_socket should be None by default

def test_httpsclientauthhandler_init_without_params():
    handler = HTTPSClientAuthHandler()
    assert handler.client_cert is None
    assert handler.client_key is None
    assert not hasattr(handler, "_unix_socket")  # _unix_socket should be None by default

def test_httpsclientauthhandler_init_with_unix_socket():
    handler = HTTPSClientAuthHandler(unix_socket="path/to/unix_socket")
    assert handler.client_cert is None
    assert handler.client_key is None
    assert handler._unix_socket == "path/to/unix_socket"

def test_build_https_connection():
    handler = HTTPSClientAuthHandler(client_cert="path/to/client_cert.pem", client_key="path/to/client_key.pem")
    with patch('urllib_request.HTTPSConnection') as mock_https:
        host = "example.com"
        handler._build_https_connection(host)
        mock_https.assert_called_with(host, cert_file="path/to/client_cert.pem", key_file="path/to/client_key.pem")

def test_build_https_connection_with_unix_socket():
    handler = HTTPSClientAuthHandler(unix_socket="path/to/unix_socket")
    with patch('ansible.module_utils.urls.UnixHTTPSConnection') as mock_unix_http:
        host = "example.com"
        handler._build_https_connection(host)
        mock_unix_http.assert_called_with("path/to/unix_socket")(host)

def test_build_https_connection_context():
    handler = HTTPSClientAuthHandler(client_cert="path/to/client_cert.pem", client_key="path/to/client_key.pem")
    with patch('urllib_request.HTTPSConnection') as mock_https:
        host = "example.com"
        handler._context = "mock_context"  # Mocking the context attribute for testing
        handler._build_https_connection(host)
        mock_https.assert_called_with(host, cert_file="path/to/client_cert.pem", key_file="path/to/client_key.pem", context="mock_context")
