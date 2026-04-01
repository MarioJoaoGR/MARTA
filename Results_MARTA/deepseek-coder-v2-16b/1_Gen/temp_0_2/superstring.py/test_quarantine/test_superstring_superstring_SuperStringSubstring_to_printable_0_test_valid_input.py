
import pytest
from superstring.superstring import SuperString, SuperStringSubstring

def test_valid_input():
    base = SuperString('Hello World')
    superstring_instance = SuperStringSubstring(base, 0, 5)
    
    assert superstring_instance._base == 'Hello World'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_to_printable_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        base = SuperString('Hello World')
        superstring_instance = SuperStringSubstring(base, 0, 5)
    
>       assert superstring_instance._base == 'Hello World'
E       AssertionError: assert <superstring.superstring.SuperString object at 0x7fd63b85ac50> == 'Hello World'
E        +  where <superstring.superstring.SuperString object at 0x7fd63b85ac50> = <superstring.superstring.SuperStringSubstring object at 0x7fd63c993250>._base

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_to_printable_0_test_valid_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_to_printable_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.04s ===============================
"""