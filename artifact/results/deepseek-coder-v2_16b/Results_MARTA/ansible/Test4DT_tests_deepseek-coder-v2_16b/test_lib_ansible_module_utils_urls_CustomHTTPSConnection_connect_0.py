
import pytest
from unittest.mock import patch
import ssl
import httplib
import socket

# Assuming HAS_SSLCONTEXT, HAS_URLLIB3_PYOPENSSLCONTEXT, and other constants are defined elsewhere in your module or environment
HAS_SSLCONTEXT = True  # Example value for demonstration purposes
HAS_URLLIB3_PYOPENSSLCONTEXT = True  # Example value for demonstration purposes
HAS_URLLIB3_SSL_WRAP_SOCKET = False  # Example value for demonstration purposes
PROTOCOL = ssl.PROTOCOL_TLSv1_2  # Example protocol version

class CustomHTTPSConnection(httplib.HTTPSConnection):
    def __init__(self, *args, **kwargs):
        httplib.HTTPSConnection.__init__(self, *args, **kwargs)
        self.context = None
        if HAS_SSLCONTEXT:
            self.context = ssl.create_default_context()
        elif HAS_URLLIB3_PYOPENSSLCONTEXT:
            from OpenSSL import SSL
            self.context = SSL.Context(PROTOCOL)
        if self.context and 'cert_file' in kwargs and 'key_file' in kwargs:
            self.context.load_cert_chain(kwargs['cert_file'], kwargs['key_file'])

    def connect(self):
        "Connect to a host on a given (SSL) port."
        if hasattr(self, 'source_address'):
            sock = socket.create_connection((self.host, self.port), self.timeout, self.source_address)
        else:
            sock = socket.create_connection((self.host, self.port), self.timeout)
        server_hostname = self.host
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
            server_hostname = self._tunnel_host
        if HAS_SSLCONTEXT or HAS_URLLIB3_PYOPENSSLCONTEXT:
            self.sock = self.context.wrap_socket(sock, server_hostname=server_hostname)
        elif HAS_URLLIB3_SSL_WRAP_SOCKET:
            from urllib3.contrib import pyopenssl
            self.sock = pyopenssl.ssl_wrap_socket(sock, keyfile=self.key_file, cert_reqs=ssl.CERT_NONE, certfile=self.cert_file, ssl_version=PROTOCOL, server_hostname=server_hostname)
        else:
            self.sock = ssl.wrap_socket(sock, keyfile=self.key_file, certfile=self.cert_file, ssl_version=PROTOCOL)

# Test cases
def test_valid_input_with_cert_and_key():
    with patch('your_module.HAS_SSLCONTEXT', True):
        conn = CustomHTTPSConnection('example.com', 443, cert_file='path/to/cert.pem', key_file='path/to/key.pem')
        assert isinstance(conn.context, ssl.SSLContext)
        assert conn.host == 'example.com'
        assert conn.port == 443
        assert conn.cert_file == 'path/to/cert.pem'
        assert conn.key_file == 'path/to/key.pem'

def test_none_values():
    with pytest.raises(TypeError):
        CustomHTTPSConnection(None, None, cert_file=None, key_file=None)

def test_invalid_input_error_handling():
    with pytest.raises(ValueError):
        conn = CustomHTTPSConnection('invalid.host', 'non-integer port', cert_file='path/to/cert.pem', key_file='path/to/key.pem')
