
import pytest
from superstring.superstring import SuperString, SuperStringSubstring

def test_edge_case_none():
    superstring_instance = SuperStringSubstring(SuperString('Hello World'), None, None)
    assert superstring_instance.to_printable() == 'Hello World'

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_to_printable_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        superstring_instance = SuperStringSubstring(SuperString('Hello World'), None, None)
>       assert superstring_instance.to_printable() == 'Hello World'

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_to_printable_0_test_edge_case_none.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
superstring.py/superstring/superstring.py:139: in to_printable
    end_index = end_index if end_index is not None else self.length()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringSubstring object at 0x7f05ed3ffdd0>

    def length(self):
>       return self._end_index - self._start_index
E       TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'

superstring.py/superstring/superstring.py:127: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_to_printable_0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.05s ===============================
"""