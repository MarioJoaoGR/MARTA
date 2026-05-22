
import pytest
from unittest.mock import patch
from httpie.models import HTTPMessage

class ValidHTTPMessage(HTTPMessage):
    def headers(self) -> str:
        return "Valid Headers"

def test_valid_headers():
    with patch('httpie.models.HTTPMessage.__init__', lambda self, orig: None):
        msg = ValidHTTPMessage("orig")
        assert msg.headers() == "Valid Headers"
