# Module: tornado.simple_httpclient
# test_simple_httpclient.py
from tornado.simple_httpclient import HTTPStreamClosedError

def test_httpstreamclosederror_init():
    try:
        raise HTTPStreamClosedError(message="The stream has been closed.")
    except HTTPStreamClosedError as e:
        assert str(e) == "The stream has been closed."

def test_httpstreamclosederror_str():
    error = HTTPStreamClosedError(message="Test message")
    assert str(error) == "Test message"
