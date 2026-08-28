
import pytest
from httpie.models import HTTPMessage

# Test cases for HTTPMessage class initialization
def test_http_message_valid_dict():
    """Test creating an instance with a valid dictionary."""
    original_message = {
        'method': 'GET',
        'url': 'http://example.com',
        'headers': {'User-Agent': 'Python/HTTPie'},
        'body': b''
    }
    http_message = HTTPMessage(original_message)
    assert isinstance(http_message, HTTPMessage)
    assert http_message._orig == original_message

def test_http_message_valid_list():
    """Test creating an instance with a valid list."""
    response_data = [
        "HTTP/1.1 200 OK",
        "Content-Type: text/plain",
        "",
        "Hello, World!"
    ]
    http_message = HTTPMessage(response_data)
    assert isinstance(http_message, HTTPMessage)