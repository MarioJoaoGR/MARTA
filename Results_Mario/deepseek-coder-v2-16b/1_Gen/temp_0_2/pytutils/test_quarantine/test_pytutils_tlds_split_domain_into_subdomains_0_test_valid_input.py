
import pytest
from pytutils.tlds import split_domain_into_subdomains

def test_valid_input():
    # Test a typical domain with subdomains
    assert split_domain_into_subdomains('this.is.a.test.skywww.net') == [
        'this.is.a.test.skywww.net',
        'is.a.test.skywww.net',
        'a.test.skywww.net',
        'test.skywww.net',
        'skywww.net'
    ]
    
    # Test a domain with the TLD included
    assert split_domain_into_subdomains('example.com', True) == [
        'example.com',
        'com'
    ]
    
    # Test a simple domain without subdomains but including the TLD
    assert split_domain_into_subdomains('skywww.net') == ['skywww.net']
    
    # Test an empty string should return an empty list
    assert split_domain_into_subdomains('') == []

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

pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test a typical domain with subdomains
        assert split_domain_into_subdomains('this.is.a.test.skywww.net') == [
            'this.is.a.test.skywww.net',
            'is.a.test.skywww.net',
            'a.test.skywww.net',
            'test.skywww.net',
            'skywww.net'
        ]
    
        # Test a domain with the TLD included
        assert split_domain_into_subdomains('example.com', True) == [
            'example.com',
            'com'
        ]
    
        # Test a simple domain without subdomains but including the TLD
        assert split_domain_into_subdomains('skywww.net') == ['skywww.net']
    
        # Test an empty string should return an empty list
>       assert split_domain_into_subdomains('') == []
E       AssertionError: assert [''] == []
E         
E         Left contains one more item: ''
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_0_test_valid_input.py:25: AssertionError
=============================== warnings summary ===============================
Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_0_test_valid_input.py::test_valid_input
  /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_0_test_valid_input.py:7: DeprecationWarning: decorating class methods with @cachedmethod is deprecated
    assert split_domain_into_subdomains('this.is.a.test.skywww.net') == [

Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_0_test_valid_input.py::test_valid_input
  /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_0_test_valid_input.py:16: DeprecationWarning: decorating class methods with @cachedmethod is deprecated
    assert split_domain_into_subdomains('example.com', True) == [

Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_0_test_valid_input.py::test_valid_input
  /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_0_test_valid_input.py:22: DeprecationWarning: decorating class methods with @cachedmethod is deprecated
    assert split_domain_into_subdomains('skywww.net') == ['skywww.net']

Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_0_test_valid_input.py::test_valid_input
  /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_0_test_valid_input.py:25: DeprecationWarning: decorating class methods with @cachedmethod is deprecated
    assert split_domain_into_subdomains('') == []

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_0_test_valid_input.py::test_valid_input
======================== 1 failed, 4 warnings in 0.15s =========================
"""