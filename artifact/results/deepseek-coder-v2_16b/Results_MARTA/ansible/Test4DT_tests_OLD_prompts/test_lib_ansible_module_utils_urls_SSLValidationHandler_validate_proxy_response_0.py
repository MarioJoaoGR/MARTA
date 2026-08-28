
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.urls import SSLValidationHandler


def test_validate_proxy_response():
    handler = SSLValidationHandler('example.com', 443, '/path/to/ca/bundle')
    with patch.object(handler, 'validate_proxy_response', return_value=None):
        response = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body>Hello World!</body></html>'
        handler.validate_proxy_response(response, valid_codes=[200])