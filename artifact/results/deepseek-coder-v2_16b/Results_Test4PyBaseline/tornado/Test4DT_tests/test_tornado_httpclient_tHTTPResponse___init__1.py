
import pytest
from unittest.mock import patch, MagicMock
from io import BytesIO
from tornado.httpclient import HTTPResponse, HTTPRequest, httputil
from tornado.httpclient import HTTPClientError, HTTPError

# Test cases for the HTTPResponse class in tornado.httpclient

def test_init_with_all_parameters():
    request = HTTPRequest("http://example.com")
    response = HTTPResponse(request=request, code=200)
    assert response.request == request
    assert response.code == 200
    assert response.reason == "OK"
    assert isinstance(response.headers, httputil.HTTPHeaders)
    assert response.buffer is None
    assert response.effective_url == request.url
    assert response.error is None
    assert response.start_time is None
    assert response.request_time is None
    assert response.time_info == {}

def test_init_with_custom_reason():
    request = HTTPRequest("http://example.com")
    response = HTTPResponse(request=request, code=404, reason="Not Found")
    assert response.code == 404
    assert response.reason == "Not Found"

def test_init_with_headers():
    request = HTTPRequest("http://example.com")
    headers = httputil.HTTPHeaders({"Content-Type": "application/json"})
    response = HTTPResponse(request=request, code=200, headers=headers)
    assert response.headers == headers

def test_init_with_buffer():
    request = HTTPRequest("http://example.com")
    buffer = BytesIO(b"test body")
    response = HTTPResponse(request=request, code=200, buffer=buffer)
    assert response.buffer == buffer

def test_init_with_effective_url():
    request = HTTPRequest("http://example.com")
    response = HTTPResponse(request=request, code=200, effective_url="http://example.com/final")
    assert response.effective_url == "http://example.com/final"

def test_init_with_error():
    request = HTTPRequest("http://example.com")
    error = HTTPClientError(404, message="Not Found", response=request)
    response = HTTPResponse(request=request, code=404, error=error)
    assert isinstance(response.error, HTTPError)
    assert response.error.code == 404
    assert response.error.message == "Not Found"

def test_init_with_request_time():
    request = HTTPRequest("http://example.com")
    response = HTTPResponse(request=request, code=200, request_time=1.5)
    assert response.request_time == 1.5

def test_init_with_time_info():
    request = HTTPRequest("http://example.com")
    time_info = {"connect": 0.3, "send": 0.2, "receive": 0.4}
    response = HTTPResponse(request=request, code=200, time_info=time_info)
    assert response.time_info == time_info

def test_init_with_default_reason():
    request = HTTPRequest("http://example.com")
    response = HTTPResponse(request=request, code=302)
    assert response.code == 302