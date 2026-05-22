
import pytest
from httpie.uploads import ChunkedMultipartUploadStream
from requests_toolbelt import MultipartEncoder
import threading
from unittest.mock import patch, MagicMock

@pytest.fixture
def setup():
    with patch('httpie.uploads.ChunkedMultipartUploadStream.__init__', return_value=None):
        encoder = MultipartEncoder(fields={'file': ('report.txt', open('report.txt', 'rb'))})
        event = threading.Event()
        upload_stream = ChunkedMultipartUploadStream(encoder, event)
        yield upload_stream

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
============================ no tests ran in 0.15s =============================
"""