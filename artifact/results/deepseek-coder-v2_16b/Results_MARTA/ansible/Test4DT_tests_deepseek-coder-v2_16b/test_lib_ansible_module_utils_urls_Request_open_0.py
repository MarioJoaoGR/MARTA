
import pytest
from ansible.module_utils.urls import Request
from urllib import request as urllib_request
from http import cookiejar
import ssl
import socket
import os
import netrc
from datetime import datetime

def test_valid_input():
    r = Request()
    response = r.open('GET', 'http://httpbin.org/cookies/set?k1=v1')
    assert response is not None
    assert response.read().decode('utf-8').find("\"cookies\": {\n    \"k1\": \"v1\"\n  }") != -1

def test_edge_case():
    r = Request(headers=None)
    with pytest.raises(ValueError):
        r.open('GET', 'http://httpbin.org/get')

def test_invalid_input():
    r = Request()
    with pytest.raises(ValueError):
        r.open('GET', 'http://httpbin.org/get', headers=123)
