
import pytest
from superstring.superstring import SuperStringLower, SuperStringBase

def test_edge_case_none():
    base = None
    superstring_lower = SuperStringLower(base)
    assert superstring_lower.character_at(0) == ''

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        base = None
        superstring_lower = SuperStringLower(base)
>       assert superstring_lower.character_at(0) == ''

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_0_test_edge_case_none.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringLower object at 0x7f594cea2850>
index = 0

    def character_at(self, index):
>       return self._base.character_at(index).lower()
E       AttributeError: 'NoneType' object has no attribute 'character_at'

superstring.py/superstring/superstring.py:159: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.05s ===============================
"""