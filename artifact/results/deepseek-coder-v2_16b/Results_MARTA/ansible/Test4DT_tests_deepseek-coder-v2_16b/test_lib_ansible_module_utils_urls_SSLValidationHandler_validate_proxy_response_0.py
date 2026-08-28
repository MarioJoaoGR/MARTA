
import pytest
from ansible.module_utils.urls import SSLValidationHandler, ProxyError


def test_ssl_validation_handler_validate_proxy_response_invalid_code():
    handler = SSLValidationHandler('example.com', 443, '/path/to/ca/bundle')
    response = b'HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/html\r\n\r\n<html><body>Hello World!</body></html>'
    with pytest.raises(ProxyError):
        handler.validate_proxy_response(response)