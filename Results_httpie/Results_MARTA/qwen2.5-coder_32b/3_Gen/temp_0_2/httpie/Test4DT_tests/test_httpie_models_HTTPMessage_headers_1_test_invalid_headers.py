
import pytest
from unittest.mock import patch
from httpie.models import HTTPMessage

class InvalidHTTPMessage(HTTPMessage):
    pass

def test_invalid_headers():
    with pytest.raises(NotImplementedError):
        invalid_message = InvalidHTTPMessage(None)
        invalid_message.headers()
