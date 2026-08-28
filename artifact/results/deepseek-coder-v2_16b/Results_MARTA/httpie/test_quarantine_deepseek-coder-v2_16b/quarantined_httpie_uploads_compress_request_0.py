
import pytest
import requests
import zlib
from httpie.uploads import compress_request

@pytest.fixture
def typical_request():
    req = requests.get('http://example.com')
    return req

def test_compress_request_with_string_body(typical_request):
    # Given a string body request
    typical_request.body = "This is the original content."
    
    # When compressing the request with always=False
    compress_request(typical_request, always=False)
    
    # Then the request should have compressed content and appropriate headers
    assert 'deflate' in typical_request.headers['Content-Encoding']
    deflater = zlib.compressobj()
    body_bytes = typical_request.body.encode()
    deflated_data = deflater.compress(body_bytes)
    deflated_data += deflater.flush()
    assert len(typical_request.body) > len(deflated_data)

def test_compress_request_with_read_body(typical_request):
    # Given a read body request
    class MockRead:
        def read(self):
            return b"This is the original content."
    typical_request.body = MockRead()
    
    # When compressing the request with always=False
    compress_request(typical_request, always=False)
    
    # Then the request should have compressed content and appropriate headers
    assert 'deflate' in typical_request.headers['Content-Encoding']
    deflater = zlib.compressobj()
    body_bytes = b"This is the original content."
    deflated_data = deflater.compress(body_bytes)
    deflated_data += deflater.flush()
    assert len(typical_request.body.read()) > len(deflated_data)

def test_compress_request_always_true(typical_request):
    # Given a request and always=True
    typical_request.body = "This is the original content."
    
    # When compressing the request with always=True
    compress_request(typical_request, always=True)
    
    # Then the request should have compressed content and appropriate headers
    assert 'deflate' in typical_request.headers['Content-Encoding']
    deflater = zlib.compressobj()
    body_bytes = b"This is the original content."
    deflated_data = deflater.compress(body_bytes)
    deflated_data += deflater.flush()
    assert len(typical_request.body) > len(deflated_data)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""