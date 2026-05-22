
import pytest
from httpie.models import HTTPMessage

class TestHTTPMessage:
    def test_init_with_invalid_type(self):
        with pytest.raises(TypeError):
            HTTPMessage("invalid input")

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

httpie/Test4DT_tests_codestral/test_httpie_models_HTTPMessage___init___0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
_________________ TestHTTPMessage.test_init_with_invalid_type __________________

self = <Test4DT_tests_codestral.test_httpie_models_HTTPMessage___init___0_test_invalid_input.TestHTTPMessage object at 0x7fe71f372750>

    def test_init_with_invalid_type(self):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

httpie/Test4DT_tests_codestral/test_httpie_models_HTTPMessage___init___0_test_invalid_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_models_HTTPMessage___init___0_test_invalid_input.py::TestHTTPMessage::test_init_with_invalid_type
============================== 1 failed in 0.19s ===============================
"""