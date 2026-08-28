
import pytest
from httpie.models import HTTPMessage

def test_http_message_iter_lines():
    with pytest.raises(NotImplementedError):
        http_message = HTTPMessage({})
        list(http_message.iter_lines(10))
