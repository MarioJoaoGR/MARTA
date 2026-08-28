
import pytest
from ansible.module_utils.urls import HTTPSClientAuthHandler
import urllib.request
import ssl
import http.client
import os

@pytest.fixture(scope="module")
def handler():
    return HTTPSClientAuthHandler(client_cert='path/to/client_cert.pem', client_key='path/to/client_key.pem')


def test_invalid_input():
    handler = HTTPSClientAuthHandler(client_cert='nonexistent/path/to/client_cert.pem', client_key='nonexistent/path/to/client_key.pem')
    opener = urllib.request.build_opener(handler)
    with pytest.raises(FileNotFoundError):
        response = opener.open('https://example.com')
