
import pytest
from unittest.mock import patch
from httpie.utils import parse_content_type_header

def test_parse_content_type_header_edge_case():
    with patch('httpie.utils.requests', autospec=True):
        header = None
        result = parse_content_type_header(header)
        assert result == ('text/html', {'charset': 'utf-8'})

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_parse_content_type_header_2_test_edge_case.py F [100%]

=================================== FAILURES ===================================
___________________ test_parse_content_type_header_edge_case ___________________

    def test_parse_content_type_header_edge_case():
        with patch('httpie.utils.requests', autospec=True):
            header = None
>           result = parse_content_type_header(header)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_parse_content_type_header_2_test_edge_case.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

header = None

    def parse_content_type_header(header):
        """Borrowed from requests."""
>       tokens = header.split(';')
E       AttributeError: 'NoneType' object has no attribute 'split'

httpie/httpie/utils.py:205: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_parse_content_type_header_2_test_edge_case.py::test_parse_content_type_header_edge_case
============================== 1 failed in 0.16s ===============================
"""