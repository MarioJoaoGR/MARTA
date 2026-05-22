
import pytest
from unittest.mock import patch
from httpie.models import HTTPMessage

class TestHTTPMessage:
    def test_invalid_metadata(self):
        msg = HTTPMessage('invalid')
        with pytest.raises(NotImplementedError):
            msg.metadata()
