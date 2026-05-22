
from httpie.output.formatters.headers import HeadersFormatter
from unittest.mock import patch

def test_valid_input():
    with patch('httpie.output.formatters.headers.HeadersFormatter.__init__', return_value=None):
        formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
        assert formatter.enabled is True

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

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_headers_HeadersFormatter___init___2_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('httpie.output.formatters.headers.HeadersFormatter.__init__', return_value=None):
            formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
>           assert formatter.enabled is True
E           AttributeError: 'HeadersFormatter' object has no attribute 'enabled'

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_headers_HeadersFormatter___init___2_test_valid_input.py:8: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_output_formatters_headers_HeadersFormatter___init___2_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""