
import pytest
from pytutils.excs import ok
from unittest import TestCase

class TestOk(TestCase):
    def test_ok(self):
        with self.assertRaises(ValueError):
            with self.assertRaises(TypeError):
                with ok(ValueError, TypeError):
                    int('abc')
                    float('abc')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_excs_ok_2_test_valid_case_with_multiple_exceptions.py F [100%]

=================================== FAILURES ===================================
________________________________ TestOk.test_ok ________________________________

self = <Test4DT_tests.test_pytutils_excs_ok_2_test_valid_case_with_multiple_exceptions.TestOk testMethod=test_ok>

    def test_ok(self):
        with self.assertRaises(ValueError):
>           with self.assertRaises(TypeError):
E           AssertionError: TypeError not raised

pytutils/Test4DT_tests/test_pytutils_excs_ok_2_test_valid_case_with_multiple_exceptions.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_excs_ok_2_test_valid_case_with_multiple_exceptions.py::TestOk::test_ok
============================== 1 failed in 0.05s ===============================
"""