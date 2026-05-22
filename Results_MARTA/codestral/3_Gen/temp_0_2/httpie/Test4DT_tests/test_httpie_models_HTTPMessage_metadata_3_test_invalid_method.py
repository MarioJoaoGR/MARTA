
import pytest
from httpie.models import HTTPMessage

class TestHTTPMessage:
    def test_invalid_method(self):
        msg = HTTPMessage('example')
        with pytest.raises(NotImplementedError):
            msg.metadata()
