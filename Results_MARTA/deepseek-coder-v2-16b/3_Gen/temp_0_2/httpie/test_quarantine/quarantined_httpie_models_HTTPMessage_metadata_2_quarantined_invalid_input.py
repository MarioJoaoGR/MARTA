
import pytest
from httpie.models import HTTPMessage

class TestHTTPMessage:
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            msg = HTTPMessage('invalid')
            msg.metadata()

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage_metadata_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________ TestHTTPMessage.test_invalid_input ______________________

self = <test_httpie_models_HTTPMessage_metadata_2_test_invalid_input.TestHTTPMessage object at 0x7fd916ca9750>

    def test_invalid_input(self):
        with pytest.raises(TypeError):
            msg = HTTPMessage('invalid')
>           msg.metadata()

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage_metadata_2_test_invalid_input.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.models.HTTPMessage object at 0x7fd916ba3a10>

    @property
    def metadata(self) -> str:
        """Return metadata about the current message."""
>       raise NotImplementedError
E       NotImplementedError

httpie/httpie/models.py:45: NotImplementedError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage_metadata_2_test_invalid_input.py::TestHTTPMessage::test_invalid_input
============================== 1 failed in 0.14s ===============================
"""