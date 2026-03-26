
# Module: superstring.superstring
import pytest
from superstring.superstring import SuperStringLower

# Test initialization with a base string
def test_init():
    str_lower = SuperStringLower("Hello World")
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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________________ test_init ___________________________________

    def test_init():
        str_lower = SuperStringLower("Hello World")
>       assert str_lower._base == "hello world"
E       AssertionError: assert 'Hello World' == 'hello world'
E         
E         - hello world
E         ? ^     ^
E         + Hello World
E         ? ^     ^

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0.py:9: AssertionError
_________________________ test_to_printable_no_indices _________________________

    def test_to_printable_no_indices():
        str_lower = SuperStringLower("Hello, World!")
>       result = str_lower.to_printable()

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringLower object at 0x7fe0e50b4b50>
start_index = None, end_index = None

    def to_printable(self, start_index=None, end_index=None):
>       return self._base.to_printable(start_index, end_index).lower()
E       AttributeError: 'str' object has no attribute 'to_printable'

superstring.py/superstring/superstring.py:162: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0.py::test_init
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0.py::test_to_printable_no_indices
============================== 2 failed in 0.05s ===============================
"""