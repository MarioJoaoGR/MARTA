
import pytest
from ssl import SSLContext
from unittest.mock import patch, MagicMock

def ensure_default_certs_loaded(ssl_context: SSLContext) -> None:
    """
    Workaround for a bug in Requests 2.32.3

    See <https://github.com/httpie/cli/issues/1583>

    """
    if hasattr(ssl_context, 'load_default_certs'):
        if not ssl_context.get_ca_certs():
            ssl_context.load_default_certs()

@pytest.fixture
def mock_ssl_context():
    with patch('ssl.SSLContext') as MockSSLContext:
        yield MockSSLContext

def test_none_input(mock_ssl_context):
    ssl_context = mock_ssl_context.return_value
    ssl_context.get_ca_certs.return_value = []  # Simulate no CA certs loaded
    
    ensure_default_certs_loaded(ssl_context)
    
    assert not hasattr(ssl_context, 'load_default_certs') or ssl_context.load_default_certs.called
