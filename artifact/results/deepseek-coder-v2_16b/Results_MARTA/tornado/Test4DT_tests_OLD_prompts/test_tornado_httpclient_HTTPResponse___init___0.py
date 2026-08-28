
import pytest
from tornado.httpclient import HTTPRequest, HTTPResponse as TornadoHTTPResponse, HTTPError
from tornado.httputil import HTTPHeaders
from io import BytesIO
import time
from unittest.mock import patch

# Test scenario 1: Successful HTTP Response with default values

# Test scenario 2: HTTP Response with custom headers and buffer
def test_http_response_with_custom_headers_and_buffer():
    request = HTTPRequest("http://example.com")
    headers = HTTPHeaders({"Content-Type": "application/json"})
    buffer = BytesIO(b"test body")
    response = TornadoHTTPResponse(request, code=200, headers=headers, buffer=buffer)
    
    assert response.code == 200
    assert response.reason == "OK"
    assert isinstance(response.headers, HTTPHeaders)
    assert response.headers["Content-Type"] == "application/json"
    assert response.effective_url == "http://example.com"
    assert response.buffer is not None
    assert response.body == b"test body"
    assert response.error is None
    assert response.request_time is None
    assert response.start_time is None
    assert isinstance(response.time_info, dict)

# Test scenario 3: HTTP Response with error (non-200 status code)

# Test scenario 4: HTTP Response with custom effective URL and request time