
import pytest
from ansible.module_utils.urls import UnixHTTPSConnection

def test_get_response():
    conn = UnixHTTPSConnection('/path/to/unix/socket')
    with pytest.raises(AttributeError):
        response = conn.get_response()

def test_post_request():
    conn = UnixHTTPSConnection('/path/to/unix/socket')
    data = {"key": "value"}
    with pytest.raises(AttributeError):
        response = conn.post_request(data)
