
import pytest
from httpie.compat import SSLContext
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
    with patch('httpie.compat.SSLContext') as MockSSLContext:
        mock_ssl = MockSSLContext.return_value
        yield mock_ssl

def test_valid_sslcontext(mock_ssl_context):
    # Arrange
    mock_ssl_context.get_ca_certs.return_value = []  # No CA certs loaded initially

    # Act
    ensure_default_certs_loaded(mock_ssl_context)

    # Assert
    assert hasattr(mock_ssl_context, 'load_default_certs')
    mock_ssl_context.load_default_certs.assert_called_once()
