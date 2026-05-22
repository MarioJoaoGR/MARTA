
import pytest
from unittest.mock import patch, Mock
from httpie.uploads import ChunkedUploadStream

@pytest.fixture(autouse=True)
def setup():
    stream = iter([b'part1', b'part2', b'part3'])
    callback = Mock()
    with patch('httpie.uploads.ChunkedUploadStream.__init__', lambda self, stream, callback: None):
        uploader = ChunkedUploadStream(stream, callback)
        for _ in range(3):
            next(uploader.stream)  # Simulate processing each chunk

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
============================ no tests ran in 0.17s =============================
"""