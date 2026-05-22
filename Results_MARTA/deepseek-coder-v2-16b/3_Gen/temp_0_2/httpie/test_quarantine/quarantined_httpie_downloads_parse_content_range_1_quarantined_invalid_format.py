
import re
from httpie.downloads import ContentRangeError, parse_content_range
import pytest

def test_invalid_format():
    with pytest.raises(ContentRangeError):
        assert parse_content_range("bytes 21010-47021/47022", 21010) == 47022

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_parse_content_range_1_test_invalid_format.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_format ______________________________

    def test_invalid_format():
>       with pytest.raises(ContentRangeError):
E       Failed: DID NOT RAISE <class 'httpie.downloads.ContentRangeError'>

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_parse_content_range_1_test_invalid_format.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_parse_content_range_1_test_invalid_format.py::test_invalid_format
============================== 1 failed in 0.20s ===============================
"""