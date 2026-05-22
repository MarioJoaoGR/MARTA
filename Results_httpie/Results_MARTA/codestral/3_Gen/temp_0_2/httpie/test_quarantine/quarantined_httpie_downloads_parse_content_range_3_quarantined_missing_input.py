
import re
from httpie.downloads import ContentRangeError, parse_content_range

def test_parse_content_range():
    # Valid content range with instance length
    assert parse_content_range("bytes 21010-47021/47022", 21010) == 47022
    
    # Valid content range without instance length (using *)
    assert parse_content_range("bytes 21010-47021/*", 21010) == '*'

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

httpie/Test4DT_tests_codestral/test_httpie_downloads_parse_content_range_3_test_missing_input.py F [100%]

=================================== FAILURES ===================================
___________________________ test_parse_content_range ___________________________

    def test_parse_content_range():
        # Valid content range with instance length
        assert parse_content_range("bytes 21010-47021/47022", 21010) == 47022
    
        # Valid content range without instance length (using *)
>       assert parse_content_range("bytes 21010-47021/*", 21010) == '*'
E       AssertionError: assert 47022 == '*'
E        +  where 47022 = parse_content_range('bytes 21010-47021/*', 21010)

httpie/Test4DT_tests_codestral/test_httpie_downloads_parse_content_range_3_test_missing_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_downloads_parse_content_range_3_test_missing_input.py::test_parse_content_range
============================== 1 failed in 0.20s ===============================
"""