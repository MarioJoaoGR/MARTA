
import pytest
from unittest.mock import patch
from httpie.models import HTTPMessage

class TestHTTPMessage:
    def test_iter_body(self):
        msg = HTTPMessage(orig={'body': b'a'*1024})
        
        with patch('httpie.models.HTTPMessage.iter_body', return_value=[b'a'] * 512):
            chunks = list(msg.iter_body(chunk_size=0))
            assert len(chunks) == 512
