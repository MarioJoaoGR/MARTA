
import pytest
from unittest.mock import patch
from httpie.models import HTTPMessage

class TestHTTPMessage:
    def test_valid_input(self):
        http_message = HTTPMessage('GET /index HTTP/1.1\r\nHost: example.com\r\n\r\n')
        with pytest.raises(NotImplementedError):
            list(http_message.iter_body(1024))

    def test_edge_case(self):
        http_message = HTTPMessage('GET /index HTTP/1.1\r\nHost: example.com\r\n\r\n')
        with pytest.raises(NotImplementedError):
            list(http_message.iter_body(0))

    def test_invalid_input(self):
        http_message = HTTPMessage('GET /index HTTP/1.1\r\nHost: example.com\r\n\r\n')
        with pytest.raises(NotImplementedError):
            list(http_message.iter_body(-1))
