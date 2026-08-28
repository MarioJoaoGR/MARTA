
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.urls import match_hostname
from ssl import SSLCertVerificationError

def test_invalid_certificate():
    with patch('ansible.module_utils.urls.match_hostname') as mock_match_hostname:
        cert = {'subjectAltName': [('DNS', 'example.org'), ('IP Address', '192.168.1.1')]}
        hostname = 'www.example.com'
        with pytest.raises(SSLCertVerificationError):
            match_hostname(cert, hostname)

def test_missing_certificate():
    cert = None
    hostname = 'www.example.com'
    with pytest.raises(ValueError):
        match_hostname(cert, hostname)
