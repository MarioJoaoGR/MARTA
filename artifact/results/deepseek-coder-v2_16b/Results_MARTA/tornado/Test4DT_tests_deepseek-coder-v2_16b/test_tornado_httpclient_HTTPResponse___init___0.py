
import pytest
from tornado.httpclient import HTTPRequest, HTTPResponse, HTTPError
from tornado.httputil import HTTPHeaders
from io import BytesIO

class TestHTTPResponse:
    def test_edge_case(self):
        request = HTTPRequest("http://example.com")
        response = HTTPResponse(request=request, code=301, headers={"Content-Type": "text/html"}, buffer=None, effective_url="http://redirected.com", error=HTTPError(404, message="Not Found"), request_time=None, time_info={}, reason=None, start_time=None)
        
        assert response.request == request
        assert response.code == 301
        assert response.headers["Content-Type"] == "text/html"
        assert response.buffer is None
        assert response.effective_url == "http://redirected.com"
        assert isinstance(response.error, HTTPError)
        assert response.request_time is None
        assert not response.time_info
        assert response.reason == "Moved Permanently"

    def test_default_error_message(self):
        request = HTTPRequest("http://example.com")
        response = HTTPResponse(request=request, code=200, headers={"Content-Type": "text/html"}, buffer=None, effective_url="http://example.com", error=None, request_time=None, time_info={}, reason=None, start_time=None)
        
        assert response.request == request
        assert response.code == 200
        assert response.headers["Content-Type"] == "text/html"
        assert response.buffer is None
        assert response.effective_url == "http://example.com"
        assert response.error is None
        assert response.request_time is None
        assert not response.time_info
        assert response.reason == "OK"
