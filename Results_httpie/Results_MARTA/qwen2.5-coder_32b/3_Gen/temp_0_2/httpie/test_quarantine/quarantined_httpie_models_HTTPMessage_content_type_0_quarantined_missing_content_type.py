
import pytest
from unittest.mock import MagicMock, patch
from httpie.models import HTTPMessage

def test_missing_content_type():
    # Create a mock HTTP message with no Content-Type header
    orig = MagicMock()
    orig.headers = {}
    
    msg = HTTPMessage(orig)
    
    assert msg.content_type() == ''

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPMessage_content_type_0_test_missing_content_type.py F [100%]

=================================== FAILURES ===================================
__________________________ test_missing_content_type ___________________________

    def test_missing_content_type():
        # Create a mock HTTP message with no Content-Type header
        orig = MagicMock()
        orig.headers = {}
    
        msg = HTTPMessage(orig)
    
>       assert msg.content_type() == ''
E       TypeError: 'str' object is not callable

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPMessage_content_type_0_test_missing_content_type.py:13: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPMessage_content_type_0_test_missing_content_type.py::test_missing_content_type
============================== 1 failed in 0.19s ===============================
"""