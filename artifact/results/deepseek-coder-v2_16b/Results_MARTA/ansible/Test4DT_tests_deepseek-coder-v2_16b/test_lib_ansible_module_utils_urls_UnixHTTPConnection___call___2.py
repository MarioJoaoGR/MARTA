
import pytest
from unittest.mock import patch
import httplib

class UnixHTTPConnection:
    def __init__(self, unix_socket):
        self._unix_socket = unix_socket

    def __call__(self, *args, **kwargs):
        httplib.HTTPConnection.__init__(self, *args, **kwargs)
        return self

def test_valid_init():
    with patch('httplib.HTTPConnection') as mock_http:
        UnixHTTPConnection('/path/to/unix/socket')
        assert mock_http.called_once_with('/path/to/unix/socket', timeout=None)

def test_invalid_init():
    with patch('httplib.HTTPConnection') as mock_http:
        UnixHTTPConnection(None)
        assert not mock_http.called

def test_error_handling():
    with pytest.raises(TypeError):
        UnixHTTPConnection('')
