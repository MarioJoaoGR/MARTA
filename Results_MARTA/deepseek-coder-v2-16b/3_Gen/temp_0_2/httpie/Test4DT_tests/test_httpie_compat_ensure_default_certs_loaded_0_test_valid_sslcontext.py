
import pytest
from httpie.compat import ensure_default_certs_loaded
from ssl import SSLContext
from unittest.mock import patch, MagicMock

@pytest.fixture(name="valid_sslcontext")
def fixture_valid_sslcontext():
    with patch('httpie.compat.ensure_default_certs_loaded'):
        ssl_context = SSLContext()
        yield ssl_context

def test_valid_sslcontext(valid_sslcontext):
    ensure_default_certs_loaded(valid_sslcontext)
    assert hasattr(valid_sslcontext, 'load_default_certs')
    assert valid_sslcontext.get_ca_certs() != []  # Ensure default certs are loaded
