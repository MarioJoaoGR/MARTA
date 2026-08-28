
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

def test_match_hostname_valid(valid_cert):
    """Test that match_hostname correctly verifies a valid hostname."""
    try:
        match_hostname(valid_cert, 'example.com')
    except CertificateError as e:
        pytest.fail(f"Certificate Error: {e}")

def test_match_hostname_invalid(invalid_cert):
    """Test that match_hostname raises a ValueError for an empty certificate."""
    with pytest.raises(ValueError):
        match_hostname(invalid_cert, 'example.com')

def test_match_hostname_no_dnsnames(valid_cert):
    """Test that match_hostname raises CertificateError when no DNS names are found."""
    valid_cert['subjectAltName'] = []
    with pytest.raises(CertificateError) as e:
        match_hostname(valid_cert, 'example.com')
    assert str(e.value) == "hostname 'example.com' doesn't match either of ['example.com', '192.168.1.1']"

def test_match_hostname_multiple_dnsnames(valid_cert):
    """Test that match_hostname raises CertificateError when multiple DNS names are found."""
    valid_cert['subjectAltName'].append(('DNS', 'anotherdomain.com'))
    with pytest.raises(CertificateError) as e:
        match_hostname(valid_cert, 'example.com')
    assert str(e.value) == "hostname 'example.com' doesn't match either of ['example.com', '192.168.1.1', 'anotherdomain.com']"

def test_match_hostname_ip_address_match(valid_cert):
    """Test that match_hostname correctly matches an IP address."""
    try:
        match_hostname(valid_cert, '192.168.1.1')
    except CertificateError as e:
        pytest.fail(f"Certificate Error: {e}")

def test_match_hostname_dnsname_mismatch(valid_cert):
    """Test that match_hostname raises CertificateError when the DNS name does not match."""
    with pytest.raises(CertificateError) as e:
        match_hostname(valid_cert, 'wrongdomain.com')
    assert str(e.value) == "hostname 'wrongdomain.com' doesn't match either of ['example.com', '192.168.1.1']"
