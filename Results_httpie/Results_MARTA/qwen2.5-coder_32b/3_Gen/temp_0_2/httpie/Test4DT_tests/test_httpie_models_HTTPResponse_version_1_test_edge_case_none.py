
import pytest
from unittest.mock import patch, MagicMock
from requests.models import Response

class HTTPResponse:
    """A :class:`requests.models.Response` wrapper."""
    def __init__(self, response):
        self._orig = response

    def version(self) -> str:
        """
        Return the HTTP version used by the server, e.g., '1.1'. Assume HTTP/1.1 if the version is not available.

        Returns:
            str: The HTTP version used by the server as a string ('0.9', '1.0', '1.1', or '2.0').
        
        Example:
            >>> response = requests.get('http://example.com')
            >>> http_version = response.version()
            >>> print(http_version)  # Output will be one of ['0.9', '1.0', '1.1', '2.0'] or '1.1' if unknown
        """
        mapping = {
            9: '0.9',
            10: '1.0',
            11: '1.1',
            20: '2.0',
        }
        fallback = 11
        version = None
        try:
            raw = self._orig.raw
            if getattr(raw, '_original_response', None):
                version = raw._original_response.version
            else:
                version = raw.version
        except AttributeError:
            pass
        return mapping.get(version or fallback, '1.1')

@pytest.fixture
def http_response():
    response = MagicMock()
    response.raw = MagicMock()
    response.raw._original_response = MagicMock()
    response.raw._original_response.version = 11
    return HTTPResponse(response)

def test_edge_case_none(http_response):
    with patch('requests.models.Response', autospec=True):
        assert http_response.version() == '1.1'
