
import pytest
from sanic import Sanic
from sanic.response import text
from sanic.headers import format_http1_response, HeaderBytesIterable




def test_status_with_empty_headers():
    headers = []
    expected_output = b'HTTP/1.1 200 OK\r\n\r\n'
    assert format_http1_response(200, headers) == expected_output