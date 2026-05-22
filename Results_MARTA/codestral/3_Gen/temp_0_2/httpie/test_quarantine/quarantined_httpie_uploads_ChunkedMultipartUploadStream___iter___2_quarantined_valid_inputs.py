
import pytest
from httpie.uploads import ChunkedMultipartUploadStream
from requests_toolbelt import MultipartEncoder
import threading

@pytest.fixture
def setup():
    encoder = MultipartEncoder(fields={'file': ('filename', b'test content')})
    event = threading.Event()
    upload_stream = ChunkedMultipartUploadStream(encoder, event)
    return upload_stream

def test_valid_inputs(setup):
    upload_stream = setup
    chunks = list(upload_stream)
    assert len(chunks) == 1
    assert chunks[0] == b'test content'

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

httpie/Test4DT_tests_codestral/test_httpie_uploads_ChunkedMultipartUploadStream___iter___2_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

setup = <httpie.uploads.ChunkedMultipartUploadStream object at 0x7f8e8c7f8650>

    def test_valid_inputs(setup):
        upload_stream = setup
        chunks = list(upload_stream)
        assert len(chunks) == 1
>       assert chunks[0] == b'test content'
E       AssertionError: assert b'--0b6ee6a96...0942a6f--\r\n' == b'test content'
E         
E         At index 0 diff: b'-' != b't'
E         Use -v to get more diff

httpie/Test4DT_tests_codestral/test_httpie_uploads_ChunkedMultipartUploadStream___iter___2_test_valid_inputs.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_uploads_ChunkedMultipartUploadStream___iter___2_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.19s ===============================
"""