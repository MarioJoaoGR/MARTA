
import pytest
from pytutils.iters import accumulate
import operator

def test_empty_list():
    iterable = []
    with pytest.raises(StopIteration):
        list(accumulate(iterable))

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

pytutils/Test4DT_tests/test_pytutils_iters_accumulate_2_test_empty_list.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_empty_list ________________________________

    def test_empty_list():
        iterable = []
>       with pytest.raises(StopIteration):
E       Failed: DID NOT RAISE <class 'StopIteration'>

pytutils/Test4DT_tests/test_pytutils_iters_accumulate_2_test_empty_list.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_iters_accumulate_2_test_empty_list.py::test_empty_list
============================== 1 failed in 0.05s ===============================
"""