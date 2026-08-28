
import pytest
from unittest.mock import patch
from httpie.models import HTTPMessage

def test_valid_input():
    with patch('httpie.models.HTTPMessage.__init__', return_value=None):
        http_message = HTTPMessage('GET /index HTTP/1.1\r\nHost: example.com\r\nContent-Type: text/html\r\n\r\n<html><body>Hello, World!</body></html>')
        assert isinstance(http_message, HTTPMessage)

def test_none_input():
    with pytest.raises(TypeError):
        with patch('httpie.models.HTTPMessage.__init__', side_effect=TypeError("Invalid input")):
            HTTPMessage(None)

def test_invalid_input():
    with pytest.raises(ValueError):
        with patch('httpie.models.HTTPMessage.__init__', side_effect=ValueError("Invalid message")):
            HTTPMessage('Invalid message')
