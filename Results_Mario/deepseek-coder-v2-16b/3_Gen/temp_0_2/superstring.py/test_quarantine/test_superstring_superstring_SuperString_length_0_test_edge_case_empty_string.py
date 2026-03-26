
import pytest
from superstring.superstring import SuperString

def test_edge_case_empty_string():
    t = SuperString('')
    assert t.split() == []

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_length_0_test_edge_case_empty_string.py F [100%]

=================================== FAILURES ===================================
_________________________ test_edge_case_empty_string __________________________

    def test_edge_case_empty_string():
        t = SuperString('')
>       assert t.split() == []
E       assert [<superstring...7faee04844d0>] == []
E         
E         Left contains one more item: <superstring.superstring.SuperString object at 0x7faee04844d0>
E         Use -v to get more diff

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_length_0_test_edge_case_empty_string.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_length_0_test_edge_case_empty_string.py::test_edge_case_empty_string
============================== 1 failed in 0.04s ===============================
"""