
# Module: sanic.response
# test_http_response.py
from sanic import HTTPResponse
import pytest

@pytest.fixture
def simple_response():
    return HTTPResponse(status=200, body="Hello, World!", content_type="text/plain")

@pytest.fixture
def response_with_custom_headers():
    headers = {"X-Custom-Header": "Value"}
    return HTTPResponse(status=200, body="Hello, World!", headers=headers, content_type="text/plain")

@pytest.fixture
def unicode_response():
    return HTTPResponse(status=200, body="Hello, World!", content_type="text/plain")

@pytest.fixture
def default_status_response():
    return HTTPResponse(body="Hello, World!", content_type="text/plain")

@pytest.fixture
def no_body_response():
    return HTTPResponse(status=200, content_type="text/plain")

def test_simple_response(simple_response):
    assert simple_response.body == b'Hello, World!'
    assert simple_response.content_type == "text/plain"
    assert simple_response.status == 200

def test_response_with_custom_headers(response_with_custom_headers):
    assert response_with_custom_headers.body == b'Hello, World!'
    assert response_with_custom_headers.content_type == "text/plain"
    assert response_with_custom_headers.status == 200
    assert response_with_custom_headers.headers["X-Custom-Header"] == "Value"

def test_unicode_response(unicode_response):
    assert unicode_response.body == b'Hello, World!'
    assert unicode_response.content_type == "text/plain"
    assert unicode_response.status == 200

def test_default_status_response(default_status_response):
    assert default_status_response.body == b'Hello, World!'
    assert default_status_response.content_type == "text/plain"
    assert default_status_response.status == 200

def test_no_body_response(no_body_response):
    assert no_body_response.body == b''
    assert no_body_response.content_type == "text/plain"
    assert no_body_response.status == 200
