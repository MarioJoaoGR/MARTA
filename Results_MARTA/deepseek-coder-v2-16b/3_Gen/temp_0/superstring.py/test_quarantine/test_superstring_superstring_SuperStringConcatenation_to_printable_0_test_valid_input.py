
import pytest
from superstring.superstring import SuperStringConcatenation, SuperStringSubstring

def test_valid_input():
    left_substr = SuperStringSubstring('Hello', 0, 5)
    right_substr = SuperStringSubstring('World!', 0, 5)
    concatenated = SuperStringConcatenation(left_substr, right_substr)
    
    assert concatenated.to_printable() == 'HelloWorld!'

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        left_substr = SuperStringSubstring('Hello', 0, 5)
        right_substr = SuperStringSubstring('World!', 0, 5)
        concatenated = SuperStringConcatenation(left_substr, right_substr)
    
>       assert concatenated.to_printable() == 'HelloWorld!'

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_valid_input.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
superstring.py/superstring/superstring.py:116: in to_printable
    return self._left.to_printable(start_index=start_index) + self._right.to_printable(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringSubstring object at 0x7f2917fc9190>
start_index = 0, end_index = 5

    def to_printable(self, start_index=None, end_index=None):
        start_index = start_index if start_index is not None else 0
        end_index = end_index if end_index is not None else self.length()
        start_index += self._start_index
        end_index += self._start_index
>       return self._base.to_printable(start_index, end_index=end_index)
E       AttributeError: 'str' object has no attribute 'to_printable'

superstring.py/superstring/superstring.py:142: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.04s ===============================
"""