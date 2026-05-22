
import pytest
from unittest.mock import patch, MagicMock
from ssl import SSLContext
from httpie.compat import ensure_default_certs_loaded

@pytest.fixture(name="valid_sslcontext")
def fixture_valid_sslcontext():
    # Create a mock SSLContext object
    mock_sslcontext = MagicMock(spec=SSLContext)
    return mock_sslcontext

def test_valid_sslcontext(valid_sslcontext):
    with patch('httpie.compat.ensure_default_certs_loaded'):
        ensure_default_certs_loaded(valid_sslcontext)
        assert hasattr(valid_sslcontext, 'load_default_certs')
        # Ensure default certs are loaded
        valid_sslcontext.get_ca_certs.return_value = []  # Mock the return value of get_ca_certs
        assert valid_sslcontext.get_ca_certs() == []
