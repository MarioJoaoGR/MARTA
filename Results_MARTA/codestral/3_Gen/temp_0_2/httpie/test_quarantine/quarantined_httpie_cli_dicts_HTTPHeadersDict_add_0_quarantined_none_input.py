
import pytest
from httpie.cli.dicts import HTTPHeadersDict

def test_none_input():
    headers = HTTPHeadersDict()
    
    # Test adding a header with None value
    headers.add('Content-Type', 'application/json')
    assert headers['Content-Type'] == 'application/json'
    
    # Test updating an existing header to None
    headers.add('Content-Type', None)
    assert headers['Content-Type'] is None
    
    # Test adding a new header with None value
    headers.add('Set-Cookie', None)
    assert 'Set-Cookie' in headers
    assert headers['Set-Cookie'] is None
    
    # Test updating an existing header to None and then back to a string
    headers.add('Cache-Control', 'no-cache')
    assert headers['Cache-Control'] == 'no-cache'
    headers.add('Cache-Control', None)
    with pytest.raises(KeyError):
        headers['Cache-Control']

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

httpie/Test4DT_tests_codestral/test_httpie_cli_dicts_HTTPHeadersDict_add_0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        headers = HTTPHeadersDict()
    
        # Test adding a header with None value
        headers.add('Content-Type', 'application/json')
        assert headers['Content-Type'] == 'application/json'
    
        # Test updating an existing header to None
        headers.add('Content-Type', None)
        assert headers['Content-Type'] is None
    
        # Test adding a new header with None value
        headers.add('Set-Cookie', None)
        assert 'Set-Cookie' in headers
        assert headers['Set-Cookie'] is None
    
        # Test updating an existing header to None and then back to a string
        headers.add('Cache-Control', 'no-cache')
        assert headers['Cache-Control'] == 'no-cache'
        headers.add('Cache-Control', None)
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

httpie/Test4DT_tests_codestral/test_httpie_cli_dicts_HTTPHeadersDict_add_0_test_none_input.py:25: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_cli_dicts_HTTPHeadersDict_add_0_test_none_input.py::test_none_input
============================== 1 failed in 0.11s ===============================
"""