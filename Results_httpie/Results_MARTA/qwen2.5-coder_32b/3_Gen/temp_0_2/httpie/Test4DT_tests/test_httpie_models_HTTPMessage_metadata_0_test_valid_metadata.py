
import pytest
from unittest.mock import patch
from httpie.models import HTTPMessage

class HttpRequest(HTTPMessage):
    def metadata(self) -> str:
        return f"Request from {self._orig['headers']['Host']}"

def test_valid_metadata():
    with patch('httpie.models.HTTPMessage.__init__', lambda self, orig: setattr(self, '_orig', orig)):
        msg = HttpRequest({'headers': {'Host': 'example.com'}})
        assert msg.metadata() == 'Request from example.com'
