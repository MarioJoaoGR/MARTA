
import pytest
from superstring.superstring import SuperString

def test_edge_cases():
    # Test with None
    s1 = SuperString(None)
    assert s1.substring(0) is None, "Expected substring to return None when content is None"

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_length_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test with None
        s1 = SuperString(None)
>       assert s1.substring(0) is None, "Expected substring to return None when content is None"

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_length_1_test_edge_cases.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
superstring.py/superstring/superstring.py:36: in substring
    end_index = end_index if end_index is not None else self.length()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperString object at 0x7f872d1fb310>

    def length(self):
        if not hasattr(self, '_length'):
>           self._length = len(self._content)
E           TypeError: object of type 'NoneType' has no len()

superstring.py/superstring/superstring.py:82: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_length_1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.05s ===============================
"""