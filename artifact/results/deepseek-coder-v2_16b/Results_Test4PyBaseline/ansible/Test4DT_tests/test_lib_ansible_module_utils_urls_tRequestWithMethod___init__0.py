
import pytest
from unittest.mock import patch
import urllib.request as urllib_request
from ansible.module_utils.urls import RequestWithMethod

# Test cases for RequestWithMethod class
def test_basic_get_request():
    with patch('urllib.request.urlopen') as mock_urlopen:
        req = RequestWithMethod('http://example.com', 'GET')
        assert req._method == 'GET'
        urllib_request.urlopen(req)
        mock_urlopen.assert_called_with(req)

def test_post_request_with_data():
    data = b'name=John&age=30'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    with patch('urllib.request.urlopen') as mock_urlopen:
        req = RequestWithMethod('http://example.com', 'POST', data, headers)
        assert req._method == 'POST'
        urllib_request.urlopen(req)
        mock_urlopen.assert_called_with(req)

def test_put_request_with_data():
    data = b'updated content'
    with patch('urllib.request.urlopen') as mock_urlopen:
        req = RequestWithMethod('http://example.com', 'PUT', data)
        assert req._method == 'PUT'
        urllib_request.urlopen(req)
        mock_urlopen.assert_called_with(req)

def test_delete_request():
    with patch('urllib.request.urlopen') as mock_urlopen:
        req = RequestWithMethod('http://example.com', 'DELETE')
        assert req._method == 'DELETE'
        urllib_request.urlopen(req)
        mock_urlopen.assert_called_with(req)

def test_custom_headers():
    headers = {'Authorization': 'Bearer token'}
    with patch('urllib.request.urlopen') as mock_urlopen:
        req = RequestWithMethod('http://example.com', 'GET', headers=headers, unverifiable=False)
        assert req._method == 'GET'
        assert req.get_header('Authorization') == 'Bearer token'
        urllib_request.urlopen(req)
        mock_urlopen.assert_called_with(req)

def test_using_origin_host():
    origin_host = 'localhost:8080'
    with patch('urllib.request.urlopen') as mock_urlopen:
        req = RequestWithMethod('http://example.com', 'GET', origin_req_host=origin_host)
        assert req._method == 'GET'