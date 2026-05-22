
import requests
import zlib
from unittest import mock

def compress_request(request, always):
    deflater = zlib.compressobj()
    
    if isinstance(request.body, str):
        body_bytes = request.body.encode()
    elif hasattr(request.body, 'read'):
        body_bytes = request.body.read()
    else:
        body_bytes = request.body
    
    deflated_data = deflater.compress(body_bytes)
    deflated_data += deflater.flush()
    
    is_economical = len(deflated_data) < len(body_bytes)
    if is_economical or always:
        request.body = deflated_data
        request.headers['Content-Encoding'] = 'deflate'
        request.headers['Content-Length'] = str(len(deflated_data))

# Example usage with mock
@mock.patch('requests.Request')
def test_compress_request(MockRequest):
    # Create a mock requests.PreparedRequest object
    mock_request = MockRequest()
    mock_request.body = b'{"key": "value"}'
    
    compress_request(mock_request, always=True)
    
    assert 'Content-Encoding' in mock_request.headers
    assert mock_request.headers['Content-Encoding'] == 'deflate'
    assert 'Content-Length' in mock_request.headers
    assert int(mock_request.headers['Content-Length']) < len(b'{"key": "value"}')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_uploads_compress_request_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
____________________________ test_compress_request _____________________________

MockRequest = <MagicMock name='Request' id='140432648677584'>

    @mock.patch('requests.Request')
    def test_compress_request(MockRequest):
        # Create a mock requests.PreparedRequest object
        mock_request = MockRequest()
        mock_request.body = b'{"key": "value"}'
    
        compress_request(mock_request, always=True)
    
>       assert 'Content-Encoding' in mock_request.headers
E       AssertionError: assert 'Content-Encoding' in <MagicMock name='Request().headers' id='140432648682832'>
E        +  where <MagicMock name='Request().headers' id='140432648682832'> = <MagicMock name='Request()' id='140432648682448'>.headers

httpie/Test4DT_tests_codestral/test_httpie_uploads_compress_request_0_test_valid_input.py:34: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_uploads_compress_request_0_test_valid_input.py::test_compress_request
============================== 1 failed in 0.18s ===============================
"""