
import pytest
from httpie.models import HTTPRequest
import requests

# Test 1: Creating an HTTPRequest object with a GET request and retrieving its body
def test_http_request_get():
    req = requests.get('http://example.com')
    http_request = HTTPRequest(req)
    assert http_request.body() == b''

# Test 2: Creating an HTTPRequest object with a POST request and retrieving its body
def test_http_request_post():
    req = requests.post('http://example.com', data={'key': 'value'})
    http_request = HTTPRequest(req)
    assert http_request.body() == b'key=value'

# Test 3: Creating an HTTPRequest object with a custom header and retrieving its body
def test_http_request_custom_header():
    req = requests.get('http://example.com', headers={'Custom-Header': 'value'})
    http_request = HTTPRequest(req)
    assert http_request.body() == b''

# Test 4: Handling a JSON request body and retrieving its encoded body
def test_http_request_json_body():
    req = requests.post('http://example.com', json={'key': 'value'})
    http_request = HTTPRequest(req)
    assert http_request.body() == b'{"key": "value"}'

# Test 5: Handling an empty body and retrieving an empty bytes object
def test_http_request_empty_body():
    req = requests.get('http://example.com')
    http_request = HTTPRequest(req)
    assert http_request.body() == b''

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""