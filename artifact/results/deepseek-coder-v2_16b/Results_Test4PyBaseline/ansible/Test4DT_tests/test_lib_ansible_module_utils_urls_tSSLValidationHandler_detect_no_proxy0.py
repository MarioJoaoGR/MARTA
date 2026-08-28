
import pytest
from unittest.mock import patch
import os
from urllib.parse import urlparse
from ansible.module_utils.urls import SSLValidationHandler

# Test initialization with default CA path
def test_sslvalidationhandler_default_ca():
    handler = SSLValidationHandler('example.com', 443)
    assert handler.hostname == 'example.com'
    assert handler.port == 443
    assert handler.ca_path is None

# Test initialization with custom CA path
def test_sslvalidationhandler_custom_ca():
    handler = SSLValidationHandler('example.com', 443, '/path/to/ca_certs')
    assert handler.hostname == 'example.com'
    assert handler.port == 443
    assert handler.ca_path == '/path/to/ca_certs'

# Test detect_no_proxy with no_proxy set
@patch('os.environ', {'no_proxy': 'localhost,127.0.0.1'})
def test_detect_no_proxy_with_no_proxy():
    handler = SSLValidationHandler('example.com', 443)
    assert not handler.detect_no_proxy('http://localhost:8080')
    assert not handler.detect_no_proxy('http://127.0.0.1:8080')
    assert handler.detect_no_proxy('https://example.com/resource')

# Test detect_no_proxy with no_proxy not set
@patch('os.environ', {'no_proxy': ''})
def test_detect_no_proxy_without_no_proxy():
    handler = SSLValidationHandler('example.com', 443)
    assert handler.detect_no_proxy('http://localhost:8080')
    assert handler.detect_no_proxy('http://127.0.0.1:8080')