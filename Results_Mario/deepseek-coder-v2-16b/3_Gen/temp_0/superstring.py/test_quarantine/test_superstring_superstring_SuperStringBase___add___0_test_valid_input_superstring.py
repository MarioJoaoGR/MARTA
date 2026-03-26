
import pytest
from superstring.superstring import SuperStringBase, SuperStringConcatenation, SuperString

def test_valid_input_superstring():
    s3 = SuperStringBase()
    result = s3 + "Hello"
    assert str(result) == "Hello", f"Expected 'Hello', but got {str(result)}"

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___add___0_test_valid_input_superstring.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_superstring _________________________

    def test_valid_input_superstring():
        s3 = SuperStringBase()
        result = s3 + "Hello"
>       assert str(result) == "Hello", f"Expected 'Hello', but got {str(result)}"

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___add___0_test_valid_input_superstring.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
superstring.py/superstring/superstring.py:66: in __str__
    return self.to_printable()
superstring.py/superstring/superstring.py:110: in to_printable
    end_index = end_index if end_index is not None else self.length()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringConcatenation object at 0x7fca63fa0e90>

    def length(self):
>       return self._left.length() + self._right.length()
E       TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

superstring.py/superstring/superstring.py:100: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___add___0_test_valid_input_superstring.py::test_valid_input_superstring
============================== 1 failed in 0.05s ===============================
"""