
import pytest
from ansible.module_utils.urls import SSLValidationHandler
import os

def test_ssl_validation_handler_custom_ca_path(monkeypatch):
    custom_ca_bundle = '/custom/ca/bundle'
    monkeypatch.setenv('SSL_CERT_FILE', custom_ca_bundle)
    handler = SSLValidationHandler('example.com', 443, ca_path=custom_ca_bundle)
    assert handler.ca_path == custom_ca_bundle

def test_ssl_validation_handler_default_ca_path():
    handler = SSLValidationHandler('example.com', 443)
    assert handler.ca_path is None
