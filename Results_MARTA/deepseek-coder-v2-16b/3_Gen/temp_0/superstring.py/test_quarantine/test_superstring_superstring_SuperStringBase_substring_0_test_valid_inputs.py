
import pytest
from superstring.superstring import SuperStringBase, SuperString, SuperStringSubstring

def test_valid_inputs():
    obj = SuperStringBase()
    
    # Test substring from start to end
    assert str(obj.substring(0, 5)) == "Hello"

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_substring_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        obj = SuperStringBase()
    
        # Test substring from start to end
>       assert str(obj.substring(0, 5)) == "Hello"

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_substring_0_test_valid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
superstring.py/superstring/superstring.py:66: in __str__
    return self.to_printable()
superstring.py/superstring/superstring.py:90: in to_printable
    end_index = end_index if end_index is not None else self.length()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperString object at 0x7ff829a08d50>

    def length(self):
        if not hasattr(self, '_length'):
>           self._length = len(self._content)
E           TypeError: object of type 'NoneType' has no len()

superstring.py/superstring/superstring.py:82: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_substring_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.05s ===============================
"""