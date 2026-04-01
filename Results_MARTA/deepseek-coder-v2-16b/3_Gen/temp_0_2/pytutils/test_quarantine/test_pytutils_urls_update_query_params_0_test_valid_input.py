
import pytest
from urllib import parse as urlparse
from urllib.parse import urlencode

def update_query_params(url, params, doseq=True):
    scheme, netloc, path, query_string, fragment = urlparse.urlsplit(url)
    query_params = urlparse.parse_qs(query_string)
    query_params.update(**params)
    new_query_string = urlencode(query_params, doseq=doseq)
    new_url = urlparse.urlunsplit([scheme, netloc, path, new_query_string, fragment])
    return new_url

def test_valid_input():
    # Test with valid URL and parameters
    original_url = 'http://example.com?foo=bar&biz=baz'
    updated_params = {'new_param': 'value'}
    expected_url = 'http://example.com?...new_param=value...'
    
    result = update_query_params(original_url, updated_params)
    assert result == expected_url

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

pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test with valid URL and parameters
        original_url = 'http://example.com?foo=bar&biz=baz'
        updated_params = {'new_param': 'value'}
        expected_url = 'http://example.com?...new_param=value...'
    
        result = update_query_params(original_url, updated_params)
>       assert result == expected_url
E       AssertionError: assert 'http://examp...w_param=value' == 'http://examp...aram=value...'
E         
E         - http://example.com?...new_param=value...
E         ?                    ^^^               ---
E         + http://example.com?foo=bar&biz=baz&new_param=value
E         ?                    ^^^^^^^^^^^^^^^^

pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.04s ===============================
"""