
import pytest
from unittest.mock import patch
from httpie.models import HTTPMessage

class TestHTTPMessage:
    def test_valid_input(self):
        with patch('httpie.models.HTTPMessage.__init__', return_value=None):
            msg = HTTPMessage({'header': 'value', 'body': 'content'})
            assert msg._orig == {'header': 'value', 'body': 'content'}

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage___init___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________ TestHTTPMessage.test_valid_input _______________________

self = <test_httpie_models_HTTPMessage___init___0_test_valid_input.TestHTTPMessage object at 0x7f2fe5b47e10>

    def test_valid_input(self):
        with patch('httpie.models.HTTPMessage.__init__', return_value=None):
            msg = HTTPMessage({'header': 'value', 'body': 'content'})
>           assert msg._orig == {'header': 'value', 'body': 'content'}
E           AttributeError: 'HTTPMessage' object has no attribute '_orig'

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage___init___0_test_valid_input.py:10: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage___init___0_test_valid_input.py::TestHTTPMessage::test_valid_input
============================== 1 failed in 0.19s ===============================
"""