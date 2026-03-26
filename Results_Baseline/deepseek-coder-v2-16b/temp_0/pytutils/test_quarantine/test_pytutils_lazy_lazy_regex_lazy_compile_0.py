
import pytest
from re import Pattern, compile as re_compile
from pytutils.lazy.lazy_regex import lazy_compile, LazyRegex

# Test the basic usage of lazy_compile with a raw regex pattern
def test_basic_usage():
    lazy_regex = lazy_compile(r'pattern')
    assert hasattr(lazy_regex._real_regex, 'findall'), "Expected _real_regex to have a method 'findall'"
    matches = lazy_regex.findall('text')  # Finds all matches using the compiled regex
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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_0.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_basic_usage _______________________________

    def test_basic_usage():
        lazy_regex = lazy_compile(r'pattern')
>       assert hasattr(lazy_regex._real_regex, 'findall'), "Expected _real_regex to have a method 'findall'"
E       AssertionError: Expected _real_regex to have a method 'findall'
E       assert False
E        +  where False = hasattr(None, 'findall')
E        +    where None = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7fdb54cafac0>._real_regex

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_0.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_0.py::test_basic_usage
============================== 1 failed in 0.05s ===============================
"""