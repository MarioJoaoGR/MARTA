
# Module: superstring.superstring
# Import the function from its module
from superstring.superstring import SuperStringUpper
import pytest

# Test case for converting the entire wrapped string to uppercase if its length is greater than or equal to 10, otherwise convert it to lowercase
def test_to_printable_entire_string():
    str_upper = SuperStringUpper("Hello World")
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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_to_printable_entire_string ________________________

    def test_to_printable_entire_string():
        str_upper = SuperStringUpper("Hello World")
>       assert str_upper.to_printable() == "HELLO WORLD"

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringUpper object at 0x7fd56d61fc10>
start_index = None, end_index = None

    def to_printable(self, start_index=None, end_index=None):
>       return self._base.to_printable(start_index, end_index).upper()
E       AttributeError: 'str' object has no attribute 'to_printable'

superstring.py/superstring/superstring.py:182: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0.py::test_to_printable_entire_string
========================= 1 failed, 1 passed in 0.05s ==========================
"""