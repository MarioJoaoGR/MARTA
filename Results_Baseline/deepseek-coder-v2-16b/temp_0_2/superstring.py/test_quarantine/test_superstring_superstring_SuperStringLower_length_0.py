
import pytest
from superstring.superstring import SuperStringLower

# Test initialization with a string
def test_init_with_string():
    obj = SuperStringLower("Hello World")
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_length_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_init_with_string _____________________________

    def test_init_with_string():
        obj = SuperStringLower("Hello World")
>       assert obj._base == "hello world"
E       AssertionError: assert 'Hello World' == 'hello world'
E         
E         - hello world
E         ? ^     ^
E         + Hello World
E         ? ^     ^

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_length_0.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_length_0.py::test_init_with_string
========================= 1 failed, 1 passed in 0.05s ==========================
"""