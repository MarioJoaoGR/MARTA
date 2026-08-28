
import pytest
from httpie.uploads import compress_request
import requests
import zlib
from unittest.mock import patch, MagicMock

def test_compress_request_with_string_body():
    with patch('zlib.compressobj', return_value=MagicMock(compress=lambda x: x)):
        req = requests.Request('GET', 'http://example.com', data="This is the original content.")
        prepared_req = req.prepare()
        compress_request(prepared_req, always=False)
        assert 'Content-Encoding' in prepared_req.headers
        assert prepared_req.headers['Content-Encoding'] == 'deflate'

def test_compress_request_with_non_string_body():
    with patch('zlib.compressobj', return_value=MagicMock(compress=lambda x: x)):
        req = requests.Request('GET', 'http://example.com')
        prepared_req = req.prepare()
        prepared_req.body = b"This is the original content."
        compress_request(prepared_req, always=False)
        assert 'Content-Encoding' in prepared_req.headers
        assert prepared_req.headers['Content-Encoding'] == 'deflate'

def test_compress_request_always_compress():
    with patch('zlib.compressobj', return_value=MagicMock(compress=lambda x: x)):
        req = requests.Request('GET', 'http://example.com', data="This is the original content.")
        prepared_req = req.prepare()
        compress_request(prepared_req, always=True)
        assert 'Content-Encoding' in prepared_req.headers
        assert prepared_req.headers['Content-Encoding'] == 'deflate'
