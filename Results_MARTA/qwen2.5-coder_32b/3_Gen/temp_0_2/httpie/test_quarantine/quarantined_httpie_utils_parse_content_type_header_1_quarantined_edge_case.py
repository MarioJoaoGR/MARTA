
import pytest
from httpie.utils import parse_content_type_header

def test_parse_content_type_header():
    # Test with a valid Content-Type header
    assert parse_content_type_header('text/html; charset=utf-8') == ('text/html', {'charset': 'utf-8'})
    
    # Test with a Content-Type header having parameters with quotes and spaces
    assert parse_content_type_header('application/json; indent="4"; charset=utf-8') == ('application/json', {'indent': '4', 'charset': 'utf-8'})
    
    # Test with None input
    with pytest.raises(TypeError):
        parse_content_type_header(None)

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_parse_content_type_header_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________ test_parse_content_type_header ________________________

    def test_parse_content_type_header():
        # Test with a valid Content-Type header
        assert parse_content_type_header('text/html; charset=utf-8') == ('text/html', {'charset': 'utf-8'})
    
        # Test with a Content-Type header having parameters with quotes and spaces
        assert parse_content_type_header('application/json; indent="4"; charset=utf-8') == ('application/json', {'indent': '4', 'charset': 'utf-8'})
    
        # Test with None input
        with pytest.raises(TypeError):
>           parse_content_type_header(None)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_parse_content_type_header_1_test_edge_case.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

header = None

    def parse_content_type_header(header):
        """Borrowed from requests."""
>       tokens = header.split(';')
E       AttributeError: 'NoneType' object has no attribute 'split'

httpie/httpie/utils.py:205: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_parse_content_type_header_1_test_edge_case.py::test_parse_content_type_header
============================== 1 failed in 0.18s ===============================
"""