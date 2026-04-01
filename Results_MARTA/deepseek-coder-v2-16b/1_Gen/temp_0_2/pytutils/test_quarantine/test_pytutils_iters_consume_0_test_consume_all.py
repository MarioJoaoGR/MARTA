
import pytest
from itertools import islice
from pytutils.iters import consume

def test_consume_all():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    
    consume(it)
    assert next(it) == 1

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

pytutils/Test4DT_tests/test_pytutils_iters_consume_0_test_consume_all.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_consume_all _______________________________

    def test_consume_all():
        lst = [1, 2, 3, 4]
        it = iter(lst)
    
        consume(it)
>       assert next(it) == 1
E       StopIteration

pytutils/Test4DT_tests/test_pytutils_iters_consume_0_test_consume_all.py:11: StopIteration
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_iters_consume_0_test_consume_all.py::test_consume_all
============================== 1 failed in 0.05s ===============================
"""