
import pytest
from unittest.mock import patch
from httpie.output.streams import RawStream

def test_valid_input():
    with patch('httpie.output.streams.RawStream.__init__', return_value=None):
        stream = RawStream(chunk_size=8192)
        assert stream.chunk_size == 8192

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_RawStream_iter_body_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('httpie.output.streams.RawStream.__init__', return_value=None):
            stream = RawStream(chunk_size=8192)
>           assert stream.chunk_size == 8192
E           AttributeError: 'RawStream' object has no attribute 'chunk_size'

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_RawStream_iter_body_0_test_valid_input.py:9: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_RawStream_iter_body_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.16s ===============================
"""