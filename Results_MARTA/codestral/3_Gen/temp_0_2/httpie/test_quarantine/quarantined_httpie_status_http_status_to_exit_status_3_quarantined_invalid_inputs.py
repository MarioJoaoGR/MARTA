
import unittest
from httpie.status import ExitStatus, http_status_to_exit_status

class TestHttpStatusToExitStatus(unittest.TestCase):
    def test_invalid_inputs(self):
        # Test with invalid HTTP status codes
        self.assertEqual(http_status_to_exit_status(100), ExitStatus.ERROR_HTTP_3XX)  # 1xx is a redirect but not followed
        self.assertEqual(http_status_to_exit_status(600), ExitStatus.ERROR_HTTP_5XX)  # 6xx is an invalid status code
        self.assertEqual(http_status_to_exit_status(-1), ExitStatus.SUCCESS)         # Negative numbers are not valid HTTP status codes
        self.assertEqual(http_status_to_exit_status(0), ExitStatus.SUCCESS)           # 0 is not a valid HTTP status code
        self.assertEqual(http_status_to_exit_status(199), ExitStatus.SUCCESS)        # 1xx but not in the range of 300-399
        self.assertEqual(http_status_to_exit_status(600), ExitStatus.ERROR_HTTP_5XX)  # 6xx is an invalid status code

if __name__ == '__main__':
    unittest.main()

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

httpie/Test4DT_tests_codestral/test_httpie_status_http_status_to_exit_status_3_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
________________ TestHttpStatusToExitStatus.test_invalid_inputs ________________

self = <Test4DT_tests_codestral.test_httpie_status_http_status_to_exit_status_3_test_invalid_inputs.TestHttpStatusToExitStatus testMethod=test_invalid_inputs>

    def test_invalid_inputs(self):
        # Test with invalid HTTP status codes
>       self.assertEqual(http_status_to_exit_status(100), ExitStatus.ERROR_HTTP_3XX)  # 1xx is a redirect but not followed
E       AssertionError: <ExitStatus.SUCCESS: 0> != <ExitStatus.ERROR_HTTP_3XX: 3>

httpie/Test4DT_tests_codestral/test_httpie_status_http_status_to_exit_status_3_test_invalid_inputs.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_status_http_status_to_exit_status_3_test_invalid_inputs.py::TestHttpStatusToExitStatus::test_invalid_inputs
============================== 1 failed in 0.14s ===============================
"""