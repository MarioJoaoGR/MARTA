
import requests
import zlib
from unittest.mock import patch, MagicMock

def compress_request(
    request: requests.PreparedRequest,
    always: bool,
):
    deflater = zlib.compressobj()
    
    if isinstance(request.body, str):
        body_bytes = request.body.encode()
    elif hasattr(request.body, 'read'):
        body_bytes = request.body.read()
    else:
        body_bytes = request.body
    
    deflated_data = deflater.compress(body_bytes) + deflater.flush()
    is_economical = len(deflated_data) < len(body_bytes)
    
    if is_economical or always:
        request.body = deflated_data
        request.headers['Content-Encoding'] = 'deflate'
        request.headers['Content-Length'] = str(len(deflated_data))

# Test case to fix the error
class TestCompressRequest:
    @patch('httpie.uploads.zlib')
    def test_compress_request_always_true(self, mock_zlib):
        # Arrange
        request = requests.PreparedRequest()
        request.body = b'large data to be compressed'
        request.headers = {}
        always = True
    
        # Mock the zlib compress function
        deflated_data = b'compressed data'
        mock_zlib.compressobj().compress.side_effect = [deflated_data, b'']
        mock_zlib.compressobj().flush.return_value = deflated_data
    
        # Act
        compress_request(request, always)
    
        # Assert
        assert request.body == deflated_data

    @patch('httpie.uploads.zlib')
    def test_compress_request_not_always_but_economical(self, mock_zlib):
        # Arrange
        request = requests.PreparedRequest()
        request.body = b'small data to be compressed'
        request.headers = {}
        always = False
    
        # Mock the zlib compress function
        deflated_data = b'compressed data'
        mock_zlib.compressobj().compress.side_effect = [deflated_data, b'']
        mock_zlib.compressobj().flush.return_value = deflated_data
    
        # Act
        compress_request(request, always)
    
        # Assert
        assert request.body == deflated_data

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

httpie/Test4DT_tests_codestral/test_httpie_uploads_compress_request_0_test_edge_case.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________ TestCompressRequest.test_compress_request_always_true _____________

self = <Test4DT_tests_codestral.test_httpie_uploads_compress_request_0_test_edge_case.TestCompressRequest object at 0x7f8ad18eb810>
mock_zlib = <MagicMock name='zlib' id='140234192194832'>

    @patch('httpie.uploads.zlib')
    def test_compress_request_always_true(self, mock_zlib):
        # Arrange
        request = requests.PreparedRequest()
        request.body = b'large data to be compressed'
        request.headers = {}
        always = True
    
        # Mock the zlib compress function
        deflated_data = b'compressed data'
        mock_zlib.compressobj().compress.side_effect = [deflated_data, b'']
        mock_zlib.compressobj().flush.return_value = deflated_data
    
        # Act
        compress_request(request, always)
    
        # Assert
>       assert request.body == deflated_data
E       AssertionError: assert b'x\x9c\xcbI,...x89\x18\n\x05' == b'compressed data'
E         
E         At index 0 diff: b'x' != b'c'
E         Use -v to get more diff

httpie/Test4DT_tests_codestral/test_httpie_uploads_compress_request_0_test_edge_case.py:46: AssertionError
_____ TestCompressRequest.test_compress_request_not_always_but_economical ______

self = <Test4DT_tests_codestral.test_httpie_uploads_compress_request_0_test_edge_case.TestCompressRequest object at 0x7f8ad14b78d0>
mock_zlib = <MagicMock name='zlib' id='140234192538640'>

    @patch('httpie.uploads.zlib')
    def test_compress_request_not_always_but_economical(self, mock_zlib):
        # Arrange
        request = requests.PreparedRequest()
        request.body = b'small data to be compressed'
        request.headers = {}
        always = False
    
        # Mock the zlib compress function
        deflated_data = b'compressed data'
        mock_zlib.compressobj().compress.side_effect = [deflated_data, b'']
        mock_zlib.compressobj().flush.return_value = deflated_data
    
        # Act
        compress_request(request, always)
    
        # Assert
>       assert request.body == deflated_data
E       AssertionError: assert b'small data to be compressed' == b'compressed data'
E         
E         At index 0 diff: b's' != b'c'
E         Use -v to get more diff

httpie/Test4DT_tests_codestral/test_httpie_uploads_compress_request_0_test_edge_case.py:65: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_uploads_compress_request_0_test_edge_case.py::TestCompressRequest::test_compress_request_always_true
FAILED httpie/Test4DT_tests_codestral/test_httpie_uploads_compress_request_0_test_edge_case.py::TestCompressRequest::test_compress_request_not_always_but_economical
============================== 2 failed in 0.13s ===============================
"""