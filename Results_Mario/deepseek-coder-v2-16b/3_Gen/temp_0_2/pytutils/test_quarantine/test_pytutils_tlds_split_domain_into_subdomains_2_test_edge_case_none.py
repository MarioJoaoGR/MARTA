
import pytest
from pytutils.tlds import split_domain_into_subdomains

def test_edge_case_none():
    # Test the function with a domain that has no subdomains and ensure it returns an empty list
    assert split_domain_into_subdomains('example.com') == []

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

pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_2_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        # Test the function with a domain that has no subdomains and ensure it returns an empty list
>       assert split_domain_into_subdomains('example.com') == []
E       AssertionError: assert ['example.com'] == []
E         
E         Left contains one more item: 'example.com'
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_2_test_edge_case_none.py:7: AssertionError
=============================== warnings summary ===============================
Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_2_test_edge_case_none.py::test_edge_case_none
  /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_2_test_edge_case_none.py:7: DeprecationWarning: decorating class methods with @cachedmethod is deprecated
    assert split_domain_into_subdomains('example.com') == []

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_2_test_edge_case_none.py::test_edge_case_none
========================= 1 failed, 1 warning in 0.18s =========================
"""