
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.urls import SSLValidationHandler
import os
from urllib.parse import urlparse

@pytest.fixture(autouse=True)
def reset_env_vars():
    # Reset the no_proxy environment variable before each test
    if 'no_proxy' in os.environ:
        del os.environ['no_proxy']

@patch('os.environ', {'no_proxy': ''})
def test_detect_no_proxy_empty():
    handler = SSLValidationHandler('example.com', 443)
    assert handler.detect_no_proxy('http://example.com') is True


@patch('os.environ', {'no_proxy': 'example.com'})
def test_detect_no_proxy_specific():
    handler = SSLValidationHandler('example.com', 443)
    assert handler.detect_no_proxy('http://example.com') is False

@patch('os.environ', {'no_proxy': 'localhost,127.0.0.1'})
def test_detect_no_proxy_with_different_url():
    handler = SSLValidationHandler('anotherdomain.com', 443)
    assert handler.detect_no_proxy('http://example.com') is True