
import pytest
from unittest.mock import patch
from httpie.models import HTTPMessage

class TestHTTPMessage:
    def test_none_input(self):
        with pytest.raises(NotImplementedError):
            msg = HTTPMessage(None)
            msg.metadata()
