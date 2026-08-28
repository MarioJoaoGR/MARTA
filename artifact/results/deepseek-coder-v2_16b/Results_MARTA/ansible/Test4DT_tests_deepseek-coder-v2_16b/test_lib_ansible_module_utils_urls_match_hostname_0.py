
import pytest
from unittest.mock import patch
from ansible.module_utils.urls import CertificateError

# Test function for scenario 1: valid certificate and hostname
def test_valid_certificate_and_hostname():
    cert = {'subjectAltName': [('DNS', 'example.com'), ('IP Address', '192.168.1.1')]}
    with pytest.raises(None) as excinfo:  # Replace None with the expected exception type if needed
        match_hostname(cert, 'example.com')
    assert str(excinfo.value) == "no appropriate commonName or subjectAltName fields were found"

# Test function for scenario 2: empty certificate
def test_empty_certificate():
    cert = None
    with pytest.raises(ValueError) as excinfo:
        match_hostname(cert, 'example.com')
    assert str(excinfo.value) == "empty or no certificate, match_hostname needs a SSL socket or SSL context with either CERT_OPTIONAL or CERT_REQUIRED"

# Test function for scenario 3: invalid hostname
def test_invalid_hostname():
    cert = {'subjectAltName': [('DNS', 'example.com'), ('IP Address', '192.168.1.1')]}
    with pytest.raises(CertificateError) as excinfo:
        match_hostname(cert, 'wronghost.com')
    assert str(excinfo.value) == "hostname %r doesn't match either of %s" % ('wronghost.com', repr(['example.com', '192.168.1.1']))
