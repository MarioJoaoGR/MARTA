
import pytest
from ansible.module_utils.urls import SSLValidationHandler
import os

# Test scenario 1: Creating an instance of SSLValidationHandler without CA path
def test_ssl_validation_handler_without_ca_path():
    handler = SSLValidationHandler('example.com', 443)
    assert handler.hostname == 'example.com'
    assert handler.port == 443
    assert handler.ca_path is None

# Test scenario 2: Creating an instance of SSLValidationHandler with CA path
def test_ssl_validation_handler_with_ca_path():
    ca_bundle_path = '/path/to/ca/bundle'
    handler = SSLValidationHandler('example.com', 443, ca_bundle_path)
    assert handler.hostname == 'example.com'
    assert handler.port == 443
    assert handler.ca_path == ca_bundle_path
