
import pytest
from unittest.mock import patch
from httpie.models import HTTPMessage

class TestHTTPMessage:
    def test_iter_body(self):
        msg = HTTPMessage(orig={'body': b'a'*1024})
        
        with patch('httpie.models.HTTPMessage.iter_body', return_value=[b'a'] * 512):
            chunks = list(msg.iter_body(chunk_size=8))
            assert len(chunks) == 64, "Expected chunk size to be correctly calculated"

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPMessage_iter_body_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
________________________ TestHTTPMessage.test_iter_body ________________________

self = <test_httpie_models_HTTPMessage_iter_body_0_test_valid_input.TestHTTPMessage object at 0x7fb1d5cdb210>

    def test_iter_body(self):
        msg = HTTPMessage(orig={'body': b'a'*1024})
    
        with patch('httpie.models.HTTPMessage.iter_body', return_value=[b'a'] * 512):
            chunks = list(msg.iter_body(chunk_size=8))
>           assert len(chunks) == 64, "Expected chunk size to be correctly calculated"
E           AssertionError: Expected chunk size to be correctly calculated
E           assert 512 == 64
E            +  where 512 = len([b'a', b'a', b'a', b'a', b'a', b'a', ...])

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPMessage_iter_body_0_test_valid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPMessage_iter_body_0_test_valid_input.py::TestHTTPMessage::test_iter_body
============================== 1 failed in 0.12s ===============================
"""