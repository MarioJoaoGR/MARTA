
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
    
    deflated_data = deflater.compress(body_bytes)
    deflated_data += deflater.flush()
    
    is_economical = len(deflated_data) < len(body_bytes)
    if is_economical or always:
        request.body = deflated_data
        request.headers['Content-Encoding'] = 'deflate'
        request.headers['Content-Length'] = str(len(deflated_data))

# Test case to fix the error
import pytest
from httpie.uploads import compress_request

@pytest.mark.parametrize("always, expected", [(True, True), (False, False)])
def test_compress_request(always, expected):
    with patch('zlib.compressobj', return_value=MagicMock()):
        request = requests.Request('POST', 'http://example.com')
        prepared_request = request.prepare()
        original_body = b'test body'
        
        if always:
            prepared_request.body = original_body
        else:
            prepared_request.body = original_body * 1000
    
        compress_request(prepared_request, always)
    
        assert 'Content-Encoding' in prepared_request.headers
        if expected:
            assert prepared_request.headers['Content-Encoding'] == 'deflate'
            assert len(prepared_request.body) < len(original_body)
        else:
            assert 'Content-Encoding' not in prepared_request.headers

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_uploads_compress_request_0_test_edge_case.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_compress_request[False-False] ______________________

always = False, expected = False

    @pytest.mark.parametrize("always, expected", [(True, True), (False, False)])
    def test_compress_request(always, expected):
        with patch('zlib.compressobj', return_value=MagicMock()):
            request = requests.Request('POST', 'http://example.com')
            prepared_request = request.prepare()
            original_body = b'test body'
    
            if always:
                prepared_request.body = original_body
            else:
                prepared_request.body = original_body * 1000
    
            compress_request(prepared_request, always)
    
            assert 'Content-Encoding' in prepared_request.headers
            if expected:
                assert prepared_request.headers['Content-Encoding'] == 'deflate'
                assert len(prepared_request.body) < len(original_body)
            else:
>               assert 'Content-Encoding' not in prepared_request.headers
E               AssertionError: assert 'Content-Encoding' not in {'Content-Length': '0', 'Content-Encoding': 'deflate'}
E                +  where {'Content-Length': '0', 'Content-Encoding': 'deflate'} = <PreparedRequest [POST]>.headers

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_uploads_compress_request_0_test_edge_case.py:50: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_uploads_compress_request_0_test_edge_case.py::test_compress_request[False-False]
========================= 1 failed, 1 passed in 0.15s ==========================
"""