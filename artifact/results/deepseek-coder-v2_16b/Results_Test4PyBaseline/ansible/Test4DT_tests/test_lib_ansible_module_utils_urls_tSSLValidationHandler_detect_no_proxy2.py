
import pytest
from unittest.mock import patch
import os
from urllib.parse import urlparse
from ansible.module_utils.urls import SSLValidationHandler

# Test detect_no_proxy with no_proxy set and URL matching a host in no_proxy
@patch('os.environ', {'no_proxy': 'localhost,127.0.0.1'})
def test_detect_no_proxy_with_matching_host():
    handler = SSLValidationHandler('example.com', 443)
    assert not handler.detect_no_proxy('http://localhost:8080')
    assert not handler.detect_no_proxy('http://127.0.0.1:8080')
    assert not handler.detect_no_proxy('https://localhost:8080')
    assert not handler.detect_no_proxy('https://127.0.0.1:8080')

# Test detect_no_proxy with no_proxy set and URL not matching any host in no_proxy
@patch('os.environ', {'no_proxy': 'localhost,127.0.0.1'})
def test_detect_no_proxy_without_matching_host():
    handler = SSLValidationHandler('example.com', 443)
    assert handler.detect_no_proxy('http://otherhost:8080')
    assert handler.detect_no_proxy('https://otherhost:8080')

# Test detect_no_proxy with no_proxy not set and URL does not match any host in no_proxy
@patch('os.environ', {'no_proxy': ''})
def test_detect_no_proxy_without_no_proxy():
    handler = SSLValidationHandler('example.com', 443)
    assert handler.detect_no_proxy('http://localhost:8080')
    assert handler.detect_no_proxy('https://127.0.0.1:8080')

# Test detect_no_proxy with no_proxy set and URL matching the netloc part of the host in no_proxy
@patch('os.environ', {'no_proxy': 'example.com'})
def test_detect_no_proxy_with_netloc_matching_host():
    handler = SSLValidationHandler('subdomain.example.com', 443)
    assert not handler.detect_no_proxy('http://subdomain.example.com:8080')
    assert not handler.detect_no_proxy('https://subdomain.example.com:8080')

# Test detect_no_proxy with no_proxy set and URL matching the netloc part of the host in no_proxy (IPv4 address)
@patch('os.environ', {'no_proxy': '127.0.0.1'})
def test_detect_no_proxy_with_netloc_ipv4():
    handler = SSLValidationHandler('example.com', 443)
    assert not handler.detect_no_proxy('http://127.0.0.1:8080')
    assert not handler.detect_no_proxy('https://127.0.0.1:8080')
