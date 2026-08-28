
import pytest
from ansible.module_utils.urls import SSLValidationHandler

def test_ssl_validation_handler_init():
    """
    Test that SSLValidationHandler can be initialized with hostname, port, and ca_path.
    """
    handler = SSLValidationHandler('example.com', 443, '/path/to/ca/bundle')
    assert handler.hostname == 'example.com'
    assert handler.port == 443
    assert handler.ca_path == '/path/to/ca/bundle'

def test_ssl_validation_handler_default_ca_path():
    """
    Test that SSLValidationHandler can be initialized without a ca_path, using default trust roots.
    """
    handler = SSLValidationHandler('example.com', 443)
    assert handler.hostname == 'example.com'
    assert handler.port == 443
    assert handler.ca_path is None
