
import pytest
from pytutils.tlds import split_domain_into_subdomains

@pytest.mark.parametrize("domain, expected", [
    ('this.is.a.test.skywww.net', ['this.is.a.test.skywww.net', 'is.a.test.skywww.net', 'a.test.skywww.net', 'test.skywww.net', 'skywww.net']),
    ('example.com', ['example.com', 'com'])
])
def test_valid_input(domain, expected):
    assert split_domain_into_subdomains(domain) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_1_test_valid_input.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________ test_valid_input[example.com-expected1] ____________________

domain = 'example.com', expected = ['example.com', 'com']

    @pytest.mark.parametrize("domain, expected", [
        ('this.is.a.test.skywww.net', ['this.is.a.test.skywww.net', 'is.a.test.skywww.net', 'a.test.skywww.net', 'test.skywww.net', 'skywww.net']),
        ('example.com', ['example.com', 'com'])
    ])
    def test_valid_input(domain, expected):
>       assert split_domain_into_subdomains(domain) == expected
E       AssertionError: assert ['example.com'] == ['example.com', 'com']
E         
E         Right contains one more item: 'com'
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_1_test_valid_input.py:10: AssertionError
=============================== warnings summary ===============================
Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_1_test_valid_input.py::test_valid_input[this.is.a.test.skywww.net-expected0]
Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_1_test_valid_input.py::test_valid_input[example.com-expected1]
  /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_1_test_valid_input.py:10: DeprecationWarning: decorating class methods with @cachedmethod is deprecated
    assert split_domain_into_subdomains(domain) == expected

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_1_test_valid_input.py::test_valid_input[example.com-expected1]
=================== 1 failed, 1 passed, 2 warnings in 0.16s ====================
"""