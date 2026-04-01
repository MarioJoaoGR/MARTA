
import pytest
from pytutils.iters import dedupe_iter

def test_edge_case_none():
    # Test that None is ignored in the iterator
    result = list(dedupe_iter([1, 2, None, 2, 3, None]))
    assert result == [1, 2, 3]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_iter_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        # Test that None is ignored in the iterator
        result = list(dedupe_iter([1, 2, None, 2, 3, None]))
>       assert result == [1, 2, 3]
E       assert [1, 2, None, 3] == [1, 2, 3]
E         
E         At index 2 diff: None != 3
E         Left contains one more item: 3
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_iter_1_test_edge_case_none.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_iters_dedupe_iter_1_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.05s ===============================
"""