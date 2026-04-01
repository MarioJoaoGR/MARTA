
import re
from pytutils.lazy.lazy_regex import LazyRegex

def test_valid_inputs():
    # Test valid regex patterns and flags
    pattern1 = r"hello"
    pattern2 = r"world"

    lazy_regex1 = LazyRegex(pattern1)
    lazy_regex2 = LazyRegex(pattern2, re.IGNORECASE)

    assert str(lazy_regex1._real_regex) == pattern1
    assert str(lazy_regex2._real_regex) == pattern2

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___init___1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test valid regex patterns and flags
        pattern1 = r"hello"
        pattern2 = r"world"
    
        lazy_regex1 = LazyRegex(pattern1)
        lazy_regex2 = LazyRegex(pattern2, re.IGNORECASE)
    
>       assert str(lazy_regex1._real_regex) == pattern1
E       AssertionError: assert 'None' == 'hello'
E         
E         - hello
E         + None

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___init___1_test_valid_inputs.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___init___1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.07s ===============================
"""