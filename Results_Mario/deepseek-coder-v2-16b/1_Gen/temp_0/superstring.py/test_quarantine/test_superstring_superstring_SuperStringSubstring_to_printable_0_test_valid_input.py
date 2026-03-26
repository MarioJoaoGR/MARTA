
import pytest
from superstring.superstring import SuperStringSubstring

def test_valid_input():
    substr = SuperStringSubstring("Hello, World!", 7, 12)
    assert substr.to_printable() == 'World!'

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
        substr = SuperStringSubstring("Hello, World!", 7, 12)
>       assert substr.to_printable() == 'World!'

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_to_printable_0_test_valid_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringSubstring object at 0x7f08d5ea6890>
start_index = 7, end_index = 12

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
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_to_printable_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""