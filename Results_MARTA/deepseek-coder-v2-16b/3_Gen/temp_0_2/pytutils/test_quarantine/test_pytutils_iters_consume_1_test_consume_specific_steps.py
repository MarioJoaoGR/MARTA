
import pytest
from itertools import islice, count
import collections
from pytutils.iters import consume

def test_consume():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    
    # Consume all elements by default
    consume(it)
    assert next(it) == 1  # The iterator should be advanced beyond the original list.
    
    # Consume specific number of steps
    lst = [1, 2, 3, 4]
    it = iter(lst)
    consume(it, 2)
    assert next(it) == 3  # The iterator should be advanced by 2 elements.
    
    # Consume more than the length of the list
    lst = [1, 2, 3, 4]
    it = iter(lst)
    consume(it, 10)
    with pytest.raises(StopIteration):
        next(it)  # The iterator should raise StopIteration as it is exhausted.

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

pytutils/Test4DT_tests/test_pytutils_iters_consume_1_test_consume_specific_steps.py F [100%]

=================================== FAILURES ===================================
_________________________________ test_consume _________________________________

    def test_consume():
        lst = [1, 2, 3, 4]
        it = iter(lst)
    
        # Consume all elements by default
        consume(it)
>       assert next(it) == 1  # The iterator should be advanced beyond the original list.
E       StopIteration

pytutils/Test4DT_tests/test_pytutils_iters_consume_1_test_consume_specific_steps.py:13: StopIteration
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_iters_consume_1_test_consume_specific_steps.py::test_consume
============================== 1 failed in 0.05s ===============================
"""