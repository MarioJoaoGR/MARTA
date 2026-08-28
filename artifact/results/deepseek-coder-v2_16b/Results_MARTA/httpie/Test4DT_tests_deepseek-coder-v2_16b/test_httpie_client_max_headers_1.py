
import pytest
from httpie.client import max_headers
import http.client

def test_max_headers_default():
    orig = http.client._MAXHEADERS
    with max_headers(None):
        assert hasattr(http.client, '_MAXHEADERS'), "Expected _MAXHEADERS to be set when limit is None"
    assert http.client._MAXHEADERS == orig, "Expected _MAXHEADERS to revert to original value when limit is None"

def test_max_headers_positive():
    orig = http.client._MAXHEADERS
    with max_headers(100):
        assert hasattr(http.client, '_MAXHEADERS'), "Expected _MAXHEADERS to be set when limit is a positive number"
    assert http.client._MAXHEADERS == orig, "Expected _MAXHEADERS to revert to original value when limit is a positive number"

def test_max_headers_zero():
    orig = http.client._MAXHEADERS
    with max_headers(0):
        assert hasattr(http.client, '_MAXHEADERS'), "Expected _MAXHEADERS to be set when limit is zero"
    assert http.client._MAXHEADERS == orig, "Expected _MAXHEADERS to revert to original value when limit is zero"
