
import pytest
from pytutils.lazy.lazy_regex import LazyRegex
import re

# Test 1: Creating a LazyRegex instance with a simple pattern
def test_simple_pattern():
    lazy_regex = LazyRegex(args=("hello.*world",))
    matches = lazy_regex.findall("hello world! hello universe!")
    assert matches == ['hello world!']

# Test 2: Creating a LazyRegex instance with a more complex pattern and ignore case flag
def test_complex_pattern():
    lazy_regex = LazyRegex(args=("new.*pattern", re.IGNORECASE))
    matches = lazy_regex.findall("another new pattern example")
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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_simple_pattern ______________________________

    def test_simple_pattern():
        lazy_regex = LazyRegex(args=("hello.*world",))
        matches = lazy_regex.findall("hello world! hello universe!")
>       assert matches == ['hello world!']
E       AssertionError: assert ['hello world'] == ['hello world!']
E         
E         At index 0 diff: 'hello world' != 'hello world!'
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___getattr___0.py::test_simple_pattern
========================= 1 failed, 1 passed in 0.06s ==========================
"""