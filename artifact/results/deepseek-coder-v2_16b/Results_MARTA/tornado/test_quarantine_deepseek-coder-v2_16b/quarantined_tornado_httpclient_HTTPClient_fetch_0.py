
import pytest
from tornado.httpclient import HTTPClient, HTTPRequest, HTTPError

class TestHTTPClient:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.http_client = HTTPClient()
    
    def test_fetch_with_url(self):
        response = self.http_client.fetch("http://www.example.com/")
        assert response.body == b"Hello, world!"  # Assuming the default response body is "Hello, world!"

    def test_fetch_with_request_object(self):
        request = HTTPRequest("http://www.example.com/", method="GET")
        response = self.http_client.fetch(request)
        assert response.body == b"Hello, world!"  # Assuming the default response body is "Hello, world!"

    def test_fetch_raises_error_on_non_200_response(self):
        request = HTTPRequest("http://www.example.com/status?code=404", method="GET")
        with pytest.raises(HTTPError) as e:
            self.http_client.fetch(request)
        assert e.value.code == 404

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""