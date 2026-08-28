
import pytest
from ansible.module_utils.urls import match_hostname, CertificateError

def test_valid_case():
    cert = {'subjectAltName': [('DNS', 'example.com'), ('IP Address', '192.168.1.1')]}
    with pytest.raises(CertificateError):
        match_hostname(cert, 'wrongdomain.com')

def test_edge_case():
    cert = None
    with pytest.raises(ValueError):
        match_hostname(cert, 'example.com')

def test_error_case():
    cert = {'subjectAltName': [('DNS', 'wrongdomain.com')]}
    with pytest.raises(CertificateError):
        match_hostname(cert, 'example.com')
