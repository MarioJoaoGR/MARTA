
import pytest
from httpie.models import HTTPMessage

def test_headers_not_implemented():
    """Test that headers method raises NotImplementedError."""
    http_message = HTTPMessage({})
    with pytest.raises(NotImplementedError):
        http_message.headers()
