
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
    # Test case with valid URL and parameters
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    expected_output = 'http://example.com?...foo=stuff...'
    
    assert update_query_params(url, params) == expected_output

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
        # Test case with valid URL and parameters
        url = 'http://example.com?foo=bar&biz=baz'
        params = {'foo': 'stuff'}
        expected_output = 'http://example.com?...foo=stuff...'
    
>       assert update_query_params(url, params) == expected_output
E       AssertionError: assert 'http://examp...stuff&biz=baz' == 'http://examp....foo=stuff...'
E         
E         - http://example.com?...foo=stuff...
E         ?                    ---         ^^^
E         + http://example.com?foo=stuff&biz=baz
E         ?                             ^^^^^^^^

pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.05s ===============================
"""