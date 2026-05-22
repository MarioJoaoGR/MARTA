
import sys
from io import StringIO
from unittest.mock import patch
from httpie.uploads import is_stdin

def test_none_input():
    with patch('sys.stdin', StringIO("")):
        assert is_stdin(sys.stdin) == True

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

httpie/Test4DT_tests_codestral/test_httpie_uploads_is_stdin_2_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with patch('sys.stdin', StringIO("")):
>           assert is_stdin(sys.stdin) == True
E           assert False == True
E            +  where False = is_stdin(<_io.StringIO object at 0x7f8b4af4a560>)
E            +    where <_io.StringIO object at 0x7f8b4af4a560> = sys.stdin

httpie/Test4DT_tests_codestral/test_httpie_uploads_is_stdin_2_test_none_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_uploads_is_stdin_2_test_none_input.py::test_none_input
============================== 1 failed in 0.17s ===============================
"""