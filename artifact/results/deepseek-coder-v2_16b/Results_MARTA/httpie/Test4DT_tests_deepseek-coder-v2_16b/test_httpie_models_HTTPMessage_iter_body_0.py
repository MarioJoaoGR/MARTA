
import pytest
from httpie.models import HTTPMessage

# Scenario 1: Test iter_body with valid chunk size
def test_valid_input():
    http_message = HTTPMessage(orig='GET /index HTTP/1.1\r\nHost: example.com\r\n\r\n')
    assert hasattr(http_message, 'iter_body')
    with pytest.raises(NotImplementedError):
        next(http_message.iter_body(chunk_size=512))

# Scenario 2: Test iter_body with chunk size of 0
def test_edge_case():
    http_message = HTTPMessage(orig='GET /index HTTP/1.1\r\nHost: example.com\r\n\r\n')
    assert hasattr(http_message, 'iter_body')
    with pytest.raises(NotImplementedError):
        next(http_message.iter_body(chunk_size=0))

# Scenario 3: Test iter_body with invalid chunk size (negative number)
def test_invalid_input():
    http_message = HTTPMessage(orig='GET /index HTTP/1.1\r\nHost: example.com\r\n\r\n')
    assert hasattr(http_message, 'iter_body')
    with pytest.raises(NotImplementedError):
        next(http_message.iter_body(chunk_size=-512))
