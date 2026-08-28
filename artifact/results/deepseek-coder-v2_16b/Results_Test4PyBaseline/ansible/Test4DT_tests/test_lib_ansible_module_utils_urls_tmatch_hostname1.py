
# Module: ansible.module_utils.urls
# test_match_hostname.py
from ansible.module_utils.urls import match_hostname, CertificateError
import pytest

@pytest.fixture
def valid_cert():
    return {
        'subjectAltName': [('DNS', 'example.com'), ('IP Address', '192.168.1.1')]
    }

@pytest.fixture
def invalid_cert():
    return {}

@pytest.fixture
def cert_no_dnsnames():
    return {'subjectAltName': []}

@pytest.fixture
def cert_multiple_dnsnames():
    return {'subjectAltName': [('DNS', 'example.com'), ('DNS', 'wildcarded.domain'), ('IP Address', '192.168.1.1')]}

@pytest.fixture
def cert_no_fields():
    return {}

# Test cases for empty certificate
def test_match_hostname_empty_cert(invalid_cert):
    """Test that match_hostname raises a ValueError for an empty certificate."""
    with pytest.raises(ValueError) as e:
        match_hostname(invalid_cert, 'example.com')
    assert str(e.value) == "empty or no certificate, match_hostname needs a SSL socket or SSL context with either CERT_OPTIONAL or CERT_REQUIRED"

# Test cases for IP address matching
def test_match_hostname_ip_address_valid():
    """Test that match_hostname correctly verifies a valid IP address."""
    cert = {'subjectAltName': [('IP Address', '192.168.1.1')]}
    try:
        match_hostname(cert, '192.168.1.1')
    except CertificateError as e:
        pytest.fail(f"Certificate Error: {e}")

def test_match_hostname_ip_address_invalid():
    """Test that match_hostname raises a CertificateError for an invalid IP address."""
    cert = {'subjectAltName': [('IP Address', '10.0.0.2')] }
    with pytest.raises(CertificateError):
        match_hostname(cert, '192.168.1.1')

# Test cases for DNS name matching
def test_match_hostname_dnsname_valid(valid_cert):
    """Test that match_hostname correctly verifies a valid hostname."""
    try:
        match_hostname(valid_cert, 'example.com')
    except CertificateError as e:
        pytest.fail(f"Certificate Error: {e}")

def test_match_hostname_dnsname_mismatch(valid_cert):
    """Test that match_hostname raises CertificateError when the DNS name does not match."""
    with pytest.raises(CertificateError) as e:
        match_hostname(valid_cert, 'wrongdomain.com')