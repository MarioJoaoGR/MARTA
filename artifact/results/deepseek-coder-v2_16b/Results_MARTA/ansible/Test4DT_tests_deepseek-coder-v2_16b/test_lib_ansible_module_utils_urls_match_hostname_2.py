
import pytest
from ansible.module_utils.urls import match_hostname, CertificateError

def test_valid_case():
    """Test standard input with valid certificate and hostname."""
    cert = {'subjectAltName': [('DNS', 'example.com')]}
    assert match_hostname(cert, 'example.com') is None

def test_edge_case():
    """Test with None input to raise ValueError."""
    with pytest.raises(ValueError):
        match_hostname(None, 'example.com')

def test_error_case():
    """Test with invalid hostname to raise CertificateError."""
    cert = {'subjectAltName': [('DNS', 'validhost.com')]}
    with pytest.raises(CertificateError):
        match_hostname(cert, 'invalidhost.com')
